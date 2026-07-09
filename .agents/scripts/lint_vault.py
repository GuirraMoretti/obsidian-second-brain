#!/usr/bin/env python3
from __future__ import annotations

import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EM_DASH = chr(0x2014)
ALLOWED_ROOT_FILES = {
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "Temas MOC.md",
    "index.md",
}
ROOT_ATTACHMENT_SUFFIXES = {
    ".avif",
    ".doc",
    ".docx",
    ".gif",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".webp",
    ".xls",
    ".xlsx",
}
ROOT_SCRIPT_SUFFIXES = {".ps1", ".py", ".sh"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def frontmatter_value(text: str, name: str) -> str:
    match = re.search(rf"(?m)^{re.escape(name)}\s*:\s*(.+?)\s*$", text)
    if not match:
        return ""
    return match.group(1).strip().strip('"').strip("'")


def has_tag(text: str, tag: str) -> bool:
    return re.search(rf"(?m)^\s*-\s*{re.escape(tag)}\s*$", text) is not None


def normalize_status(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "-")
    decomposed = unicodedata.normalize("NFD", normalized)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def has_index_link(index_text: str, base_name: str) -> bool:
    return re.search(rf"\[\[{re.escape(base_name)}(?=\]\]|\||#)", index_text) is not None


def resolve_wikilink(raw_target: str, known_targets: set[str]) -> bool:
    if not raw_target.strip() or raw_target.startswith("#"):
        return True

    target = raw_target.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")
    if not target:
        return True

    target_no_md = target[:-3] if target.endswith(".md") else target
    target_base = Path(target).stem

    return any(candidate in known_targets for candidate in (target, target_no_md, target_base))


def markdown_files_under(*folder_names: str) -> list[Path]:
    files: list[Path] = []
    for folder_name in folder_names:
        folder = ROOT / folder_name
        if folder.exists():
            files.extend(folder.rglob("*.md"))
    return files


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    suggestions: list[str] = []

    index_path = ROOT / "index.md"
    index_text = read_text(index_path) if index_path.exists() else ""

    active_notes = sorted(
        (ROOT / "Ativo").glob("*.md"),
        key=lambda path: path.name.casefold(),
    )
    active_notes = [path for path in active_notes if path.name != "backlog.md"]

    moc_notes: list[Path] = []
    for folder_name in ("Ativo", "Arquivo"):
        folder = ROOT / folder_name
        if folder.exists():
            moc_notes.extend(folder.rglob("*- MOC.md"))

    for root_file in sorted((path for path in ROOT.iterdir() if path.is_file()), key=lambda path: path.name.casefold()):
        if root_file.name in ALLOWED_ROOT_FILES:
            continue
        if root_file.suffix.lower() in ROOT_ATTACHMENT_SUFFIXES:
            errors.append(
                f"Anexo solto na raiz: {rel(root_file)} -> mover para Arquivo/attachments/"
            )
        elif root_file.suffix.lower() in ROOT_SCRIPT_SUFFIXES:
            suggestions.append(
                f"Script solto na raiz: {rel(root_file)} -> mover para .agents/scripts/"
            )
        else:
            suggestions.append(f"Arquivo inesperado na raiz: {rel(root_file)}")

    for note in active_notes:
        text = read_text(note)
        base = note.stem
        description = frontmatter_value(text, "description")
        status = frontmatter_value(text, "status")

        if not has_index_link(index_text, base):
            errors.append(f"Ativo ausente no index: {rel(note)}")

        if not description:
            errors.append(f"Nota ativa sem description: {rel(note)}")

        if not has_tag(text, "papel/raiz"):
            errors.append(f"Nota em Ativo sem papel/raiz: {rel(note)}")

        line_match = re.search(rf"(?m)^.*\[\[{re.escape(base)}(?=\]\]|\||#).*$", index_text)
        if line_match and EM_DASH in line_match.group(0):
            parts = [part.strip() for part in line_match.group(0).split(EM_DASH)]
            if len(parts) >= 3:
                index_status = parts[1]
                if normalize_status(status) != normalize_status(index_status):
                    errors.append(
                        f"Status divergente: {rel(note)} usa '{status}', mas index exibe '{index_status}'"
                    )

    for moc in moc_notes:
        text = read_text(moc)
        if not frontmatter_value(text, "description"):
            errors.append(f"MOC sem description: {rel(moc)}")
        if not has_tag(text, "papel/moc"):
            errors.append(f"MOC sem papel/moc: {rel(moc)}")

    known_targets: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.relative_to(ROOT).parts)
        if ".git" in parts or ".obsidian" in parts:
            continue

        relative = rel(path)
        known_targets.add(path.stem)
        known_targets.add(relative)
        if path.suffix == ".md":
            known_targets.add(relative[:-3])

    scan_files = markdown_files_under("Ativo", "Arquivo", "Diario")
    if index_path.exists():
        scan_files.append(index_path)
    temas_path = ROOT / "Temas MOC.md"
    if temas_path.exists():
        scan_files.append(temas_path)

    unique_scan_files = sorted(set(scan_files), key=lambda path: rel(path).casefold())
    link_pattern = re.compile(r"\[\[([^\]]+)\]\]")

    for path in unique_scan_files:
        text = read_text(path)
        for match in link_pattern.finditer(text):
            target = match.group(1)
            if not resolve_wikilink(target, known_targets):
                warnings.append(f"Wikilink sem alvo: {rel(path)} -> [[{target}]]")

    markdown_text = {path: read_text(path) for path in unique_scan_files}
    for note in active_notes:
        inbound_pattern = re.compile(rf"\[\[{re.escape(note.stem)}(?=\]\]|\||#)")
        has_inbound = any(
            path != note and inbound_pattern.search(text)
            for path, text in markdown_text.items()
        )
        if not has_inbound:
            suggestions.append(f"Nota ativa potencialmente orfa: {rel(note)}")

    print("# Lint Vault\n")
    print(f"## Erros ({len(errors)})")
    if errors:
        for item in errors:
            print(f"- {item}")
    else:
        print("- Nenhum erro critico encontrado.")

    print(f"\n## Alertas ({len(warnings)})")
    if warnings:
        for item in warnings:
            print(f"- {item}")
    else:
        print("- Nenhum alerta encontrado.")

    print(f"\n## Sugestoes ({len(suggestions)})")
    if suggestions:
        for item in suggestions:
            print(f"- {item}")
    else:
        print("- Nenhuma sugestao encontrada.")


if __name__ == "__main__":
    main()
