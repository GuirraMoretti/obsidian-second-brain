import os
import sys
import re
import json
import urllib.request
import urllib.error
import shutil

# Path definitions
vault_path = r"c:\Users\Gui.ABC\Documents\GitHub\obsidian"
fontes_dir = os.path.join(vault_path, "Fontes")
inbox_dir = os.path.join(vault_path, "Inbox")

# Ensure Fontes directory exists
os.makedirs(fontes_dir, exist_ok=True)

def clean_filename(title):
    # Remove characters that are not letters, numbers, spaces, underscores, or dashes
    clean = re.sub(r'[^\w\s-]', '', title)
    # Replace spaces and multiple dashes/underscores with a single underscore
    clean = re.sub(r'[\s_-]+', '_', clean)
    return clean.strip('_') + ".pdf"

def download_file(url, dest_path):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        with open(dest_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

def resolve_doi(doi):
    print(f"Resolving DOI: {doi}", file=sys.stderr)
    api_url = f"https://api.unpaywall.org/v2/{doi}?email=antigravity-agent@gmail.com"
    
    try:
        req = urllib.request.Request(api_url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        title = data.get("title", "Estudo Sem Titulo")
        year = data.get("year", "")
        doi_url = data.get("doi_url", f"https://doi.org/{doi}")
        
        # Format authors
        authors_list = data.get("z_authors", [])
        if not authors_list:
            authors_list = data.get("authors", [])
        authors = ", ".join([a.get("family", "") for a in authors_list if a.get("family")])
        if not authors:
            authors = "Desconhecido"

        is_oa = data.get("is_oa", False)
        pdf_url = None
        if is_oa:
            pdf_url = data.get("best_oa_location", {}).get("url_for_pdf")
            
        if pdf_url:
            filename = clean_filename(title)
            dest_path = os.path.join(fontes_dir, filename)
            print(f"Downloading PDF from {pdf_url} to {dest_path}", file=sys.stderr)
            try:
                download_file(pdf_url, dest_path)
                return {
                    "status": "success",
                    "downloaded": True,
                    "filepath": f"Fontes/{filename}",
                    "title": title,
                    "year": year,
                    "authors": authors,
                    "doi_url": doi_url
                }
            except Exception as e:
                print(f"Download failed from {pdf_url}: {e}. Falling back to metadata only.", file=sys.stderr)
                
        # Return metadata only if paywalled or download failed
        return {
            "status": "success",
            "downloaded": False,
            "reason": "paywall" if not is_oa else "download_error",
            "title": title,
            "year": year,
            "authors": authors,
            "doi_url": doi_url
        }
    except Exception as e:
        print(f"DOI resolution error: {e}", file=sys.stderr)
        return {"status": "error", "message": f"Erro de resolucao de DOI: {str(e)}"}

def process_url_pdf(url):
    print(f"Processing direct PDF URL: {url}", file=sys.stderr)
    # Extract filename from URL
    url_path = urllib.parse.urlparse(url).path
    filename = os.path.basename(url_path)
    if not filename.endswith('.pdf'):
        filename = "artigo_downloaded.pdf"
    
    filename = clean_filename(filename.replace(".pdf", ""))
    dest_path = os.path.join(fontes_dir, filename)
    
    try:
        download_file(url, dest_path)
        return {
            "status": "success",
            "downloaded": True,
            "filepath": f"Fontes/{filename}",
            "title": filename.replace(".pdf", "").replace("_", " ")
        }
    except Exception as e:
        return {"status": "error", "message": f"Erro ao baixar PDF da URL: {str(e)}"}

def process_local_file(filename):
    print(f"Processing local file: {filename}", file=sys.stderr)
    src_path = os.path.join(inbox_dir, filename)
    if not os.path.exists(src_path):
        # Check if it's already in Fontes
        fontes_path = os.path.join(fontes_dir, filename)
        if os.path.exists(fontes_path):
            return {
                "status": "success",
                "downloaded": True,
                "filepath": f"Fontes/{filename}",
                "title": filename.replace(".pdf", "").replace("_", " ")
            }
        return {"status": "error", "message": f"Arquivo nao encontrado na Inbox: {filename}"}
        
    dest_filename = clean_filename(filename.replace(".pdf", ""))
    dest_path = os.path.join(fontes_dir, dest_filename)
    
    try:
        shutil.move(src_path, dest_path)
        return {
            "status": "success",
            "downloaded": True,
            "filepath": f"Fontes/{dest_filename}",
            "title": dest_filename.replace(".pdf", "").replace("_", " ")
        }
    except Exception as e:
        return {"status": "error", "message": f"Erro ao mover arquivo local: {str(e)}"}

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Nenhuma entrada fornecida."}))
        sys.exit(1)
        
    input_str = sys.argv[1].strip()
    
    # 1. Check if direct PDF URL
    if input_str.startswith("http") and (input_str.endswith(".pdf") or ".pdf?" in input_str):
        res = process_url_pdf(input_str)
    # 2. Check if DOI URL or raw DOI
    elif "doi.org/" in input_str or re.match(r'^10\.\d{4,9}/', input_str):
        # Extract DOI
        doi_match = re.search(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', input_str, re.IGNORECASE)
        if doi_match:
            res = resolve_doi(doi_match.group(1))
        else:
            res = {"status": "error", "message": "Nao foi possivel extrair o DOI da entrada."}
    # 3. Assume local file in Inbox
    else:
        res = process_local_file(input_str)
        
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
