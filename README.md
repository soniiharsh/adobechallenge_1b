# 🤖 Challenge 1b: Multi-Collection PDF Analysis 📚🧠

## 🚀 Overview

This project analyzes multiple PDF collections and extracts the most relevant content based on a given **persona** and **job-to-be-done (JTBD)**. It ranks content by semantic relevance using NLP models and generates structured JSON output. Optimized for quick processing and extensibility, this system is ideal for document intelligence tasks in real-world scenarios.

---

## ✅ Features

- 👤 Persona-aware analysis  
- 🧠 NLP-powered concept extraction and ranking  
- 📝 Query-focused summarization  
- 📄 Outputs valid JSON with section highlights  
- 📁 Supports multiple document collections  
- 📦 JSON schema validation  
- 🐳 Docker-compatible architecture

---

## 📦 Project Structure

```
Challenge_1b/
├── Collection 1/                  
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection 2/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection 3/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── src/
│   ├── main.py                    # Main execution pipeline
│   ├── nlp_processor.py          # Persona embedding and concept extractor
│   ├── extractor.py              # PDF text & section extractor
│   ├── summarizer.py             # Query-focused summary builder
│   ├── json_generator.py         # Output JSON builder
│   └── utils.py                  # Utility functions
├── test_data/
│   ├── sample_input.json
│   └── sample_output.json
├── challenge1b_output_schema.json
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📥 Input Format (`challenge1b_input.json`)

```json
{
  "challenge_info": {
    "challenge_id": "round_1b_002",
    "test_case_name": "south_france_trip"
  },
  "documents": [
    { "filename": "guide1.pdf", "title": "Provence Travel Guide" },
    { "filename": "guide2.pdf", "title": "French Riviera Must-Sees" }
  ],
  "persona": {
    "role": "Travel Planner"
  },
  "job_to_be_done": {
    "task": "Plan a 4-day trip for 10 college friends to the South of France"
  }
}
```

---

## 📤 Output Format (`challenge1b_output.json`)

```json
{
  "metadata": {
    "input_documents": ["guide1.pdf", "guide2.pdf"],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a 4-day trip for 10 college friends to the South of France",
    "processing_timestamp": "2025-07-28T16:45:00"
  },
  "extracted_sections": [
    {
      "document": "guide2.pdf",
      "section_title": "Top 10 Experiences in French Riviera",
      "importance_rank": 1,
      "page_number": 5
    }
  ],
  "subsection_analysis": [
    {
      "document": "guide2.pdf",
      "refined_text": "Must-visit locations include Nice, Cannes, Antibes, and the coastal train journey...",
      "page_number": 5
    }
  ]
}
```

---

## 🧠 How It Works

1. Extracts all section text from PDFs using `PyMuPDF`
2. Embeds persona + JTBD using `SentenceTransformers`
3. Computes semantic relevance between section text and concepts
4. Ranks most relevant sections
5. Summarizes the top-ranked content using query-focused extraction
6. Outputs structured JSON with metadata, ranked sections, and summaries

---

## ▶️ Run the System Locally

1. 📦 Install dependencies:
```bash
pip install -r requirements.txt
```

2. 📁 Place PDFs inside any `CollectionX/PDFs/` folder.

3. 🚀 Run the pipeline:
```bash
python src/main.py
```

> It will prompt for input and output JSON files and generate structured output.

---

## 🐳 Run Using Docker

1. 🏗️ Build the image:
```bash
docker build -t pdf-analysis .
```

2. 🚀 Run the container:
```bash
docker run --rm -v $(pwd)/Collection1:/app/Collection1 pdf-analysis
```

> Replace `Collection1` with the one you want to process. Output JSON will be saved inside the same collection folder.

---

## 🧪 Testing & Validation

To validate output JSON against the schema:
```bash
python src/utils.py --validate output.json --schema challenge1b_output_schema.json
```

---

## 🧩 Example Use Cases

| Collection    | Persona           | JTBD Description                                                         |
|---------------|-------------------|--------------------------------------------------------------------------|
| Collection 1  | Travel Planner     | Plan a 4-day itinerary for South of France                               |
| Collection 2  | HR Professional    | Learn how to build fillable forms using Acrobat for onboarding           |
| Collection 3  | Food Contractor    | Design a vegetarian buffet dinner for a corporate gathering              |

---

## 🛠 Troubleshooting

| Issue                  | Fix                                                             |
|------------------------|------------------------------------------------------------------|
| No relevant sections   | Use higher-quality or well-formatted PDF documents               |
| Docker fails           | Check Docker is installed and internet access is available       |
| Output not generated   | Ensure input JSON format is valid and PDFs are readable          |

---

## 🙌 Contributions

Pull requests are welcome! Please open issues for discussion before making major changes.

---

## 📜 License

MIT License — free for personal, academic, or commercial use.

---

## 👤 Author

- Harsh Soni  
- Adobe Hackathon 2025 — Challenge 1b
