import requests
import os

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

pdf_folder = "../data/pdfs"
xml_folder = "../data/xml"

os.makedirs(xml_folder, exist_ok=True)

for pdf in os.listdir(pdf_folder):
    with open(os.path.join(pdf_folder, pdf), 'rb') as f:
        files = {'input': f}
        r = requests.post(GROBID_URL, files=files)

    output_file = os.path.join(xml_folder, pdf.replace(".pdf",".xml"))

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(r.text)