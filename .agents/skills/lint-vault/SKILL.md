---
name: lint-vault
description: Realiza a auditoria periódica de saúde, consistência e integridade do cofre (detectando contradições, notas órfãs, links perdidos ou conceitos não resolvidos).
---

# Habilidade: Auditoria do Cofre (Lint Vault)

Esta habilidade orienta o subagente agy a escanear a base de conhecimento do cofre para propor melhorias de coesão, consertar links quebrados e detectar dados conflitantes ou obsoletos.

## Diretrizes de Execução

Quando o usuário solicitar um lint, auditoria ou verificação de saúde do cofre (ex: *"Faça o lint do cofre"*):

1. **Executar Script de Diagnostico:** Rode `python .agents/scripts/lint_vault.py` a partir da raiz do cofre (use `python3` se este for o comando do ambiente Linux/macOS). O script e a fonte primaria para os checks mecanicos.
2. **Escopo do Script:** Use o relatorio gerado para avaliar:
   *   notas em `Ativo/` ausentes no `index.md`;
   *   notas em `Ativo/` sem `description`;
   *   notas em `Ativo/` sem `papel/raiz`;
   *   MOCs (`*- MOC.md`) sem `description`;
   *   MOCs (`*- MOC.md`) sem `papel/moc`;
   *   anexos soltos na raiz que devem ir para `Arquivo/attachments/`;
   *   scripts soltos na raiz que devem ir para `.agents/scripts/`;
   *   wikilinks que nao resolvem para nenhum arquivo conhecido;
   *   notas potencialmente orfas sem inbound link;
   *   divergencias entre status do frontmatter e status exibido no `index.md`.
3. **Leitura Complementar:** Quando o script apontar uma divergencia sem contexto suficiente, leia os arquivos afetados antes de propor correcao. Nao altere status nem marque tarefas como concluidas sem sinal explicito do usuario.
4. **Apresentacao de Relatorio:** Exiba no chat um resumo estruturado com `Erros`, `Alertas` e `Sugestoes`, preservando os itens acionaveis do script.
5. **Proposta de Acao:** Pergunte se o usuario deseja que voce corrija os itens listados automaticamente.
6. **Log (Silencioso):** Registre a verificacao no `.agents/assistant/logs.md` (ex: `## [AAAA-MM-DD] lint | Script executado. Erros: X | Alertas: Y | Sugestoes: Z`).
