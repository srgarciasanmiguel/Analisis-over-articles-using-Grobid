import requests
import time
import os

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

pdf_dir = "data/pdf"
xml_dir = "data/xml"

os.makedirs(xml_dir, exist_ok=True)

pdf_files = [
    f for f in os.listdir(pdf_dir)
    if f.lower().endswith(".pdf") and os.path.isfile(os.path.join(pdf_dir, f))]

for i, pdf in enumerate(pdf_files, 1):
    start = time.time()

    print(f"[{i}/{len(pdf_files)}] Procesando {pdf}")

    pdf_path = os.path.join(pdf_dir, pdf)

    with open(pdf_path, "rb") as f:
        files = {"input": f}
        r = requests.post(GROBID_URL, files=files)

    output_file = os.path.join(xml_dir, pdf.replace(".pdf", ".xml"))

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(r.text)

    elapsed = round(time.time() - start, 2)

    print(f"✔ Terminado en {elapsed}s\n")