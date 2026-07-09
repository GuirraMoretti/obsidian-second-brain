import PyPDF2
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
pdf_file = open(root / 'Arquivo' / 'attachments' / 'daad_epos_deadlines.pdf', 'rb')
read_pdf = PyPDF2.PdfReader(pdf_file)

for page_num in range(len(read_pdf.pages)):
    page = read_pdf.pages[page_num]
    text = page.extract_text()
    if 'HTW' in text or 'Berlin' in text or 'Project Management' in text:
        print(f'--- Page {page_num + 1} ---')
        lines = text.split('\n')
        for idx, line in enumerate(lines):
            if 'HTW' in line or 'Project' in line or 'Berlin' in line:
                start = max(0, idx - 2)
                end = min(len(lines), idx + 3)
                for i in range(start, end):
                    print(lines[i])
                print('-' * 20)
pdf_file.close()
