import os
import json
from datetime import datetime
import fitz  # PyMuPDF

OUTPUT_DIR = "../test_data"
PDF_DIR = "../Collection 1/PDFs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sample_output.json")


def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            sections.append({
                "document": os.path.basename(pdf_path),
                "section_title": f"Page {i+1}",
                "text": text,
                "page_number": i + 1
            })
    return sections


def generate_output(pdf_files):
    all_sections = []
    for pdf in pdf_files:
        all_sections.extend(extract_sections(pdf))

    metadata = {
        "input_documents": [os.path.basename(p) for p in pdf_files],
        "persona": "Travel Planner",
        "job_to_be_done": "Plan a 4-day trip for 10 college friends to South of France",
        "processing_timestamp": datetime.now().isoformat()
    }

    output = {
        "metadata": metadata,
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for idx, sec in enumerate(all_sections[:5]):
        output["extracted_sections"].append({
            "document": sec["document"],
            "section_title": sec["section_title"],
            "importance_rank": idx + 1,
            "page_number": sec["page_number"]
        })

        output["subsection_analysis"].append({
            "document": sec["document"],
            "refined_text": sec["text"][:300] + "...",
            "page_number": sec["page_number"]
        })

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=4)

    print(f"✅ Output written to {OUTPUT_FILE}")


def main():
    print("📄 Scanning for PDFs in:", PDF_DIR)
    pdfs = [os.path.join(PDF_DIR, f) for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]
    if not pdfs:
        print("❌ No PDFs found!")
        return
    generate_output(pdfs)


if __name__ == "__main__":
    main()
