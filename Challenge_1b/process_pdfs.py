import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    path = "sample.pdf"
    if os.path.exists(path):
        print(extract_text_from_pdf(path))
    else:
        print("No sample PDF found.")
