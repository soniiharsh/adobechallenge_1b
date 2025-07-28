# 📘 Challenge 1b: Approach Explanation

This document outlines the methodology and architecture used for solving the Multi-Collection PDF Analysis problem.

---

## 🎯 Objective

To develop a robust and generalizable document intelligence system that:
- Parses and processes multiple collections of PDFs
- Understands user "personas" and "jobs-to-be-done" (JTBD)
- Extracts and ranks relevant content
- Outputs results in a structured JSON format

---

## 🧱 System Architecture

### 1. **PDF Parsing**
- Uses `PyMuPDF` to extract text and layout metadata from each page.
- Heuristics detect section titles based on font size, boldness, and keywords.

### 2. **NLP-Powered Relevance Scoring**
- `spaCy` is used for linguistic processing and noun-chunk extraction from JTBD.
- `SentenceTransformers` (MiniLM) encodes section texts and JTBD concepts into semantic vectors.
- Cosine similarity is calculated to rank sections by relevance.

### 3. **Query-Focused Summarization**
- Selects the top sentences from each section that are semantically similar to JTBD concepts.

### 4. **Structured JSON Output**
- Final output includes:
  - `metadata`: persona, task, timestamp
  - `extracted_sections`: top 5 ranked sections
  - `subsection_analysis`: refined summaries

### 5. **Schema Validation**
- Uses `jsonschema` to validate all outputs against a strict JSON schema for quality assurance.

---

## ⚙️ Collection Examples

| Collection | Persona            | JTBD                                                           |
|------------|--------------------|----------------------------------------------------------------|
| 1          | Travel Planner     | Plan 4-day trip to South of France for 10 college friends      |
| 2          | HR Professional    | Manage onboarding forms using Adobe Acrobat                    |
| 3          | Food Contractor    | Prepare vegetarian buffet-style menu for a corporate event     |

---

## 🐳 Optional: Docker Support
- Includes a `Dockerfile` for containerized setup
- Allows clean and portable deployment

---

## ✅ Why This Approach Works

- It separates concerns: parsing, scoring, summarization, and output formatting.
- It is domain-agnostic: works across travel, food, HR, and academic PDFs.
- It is scalable: easily extendable to more collections or smarter ranking models.

