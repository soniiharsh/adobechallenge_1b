import os
import json

def list_pdfs(folder_path):
    """Return list of all PDF file paths in the given folder."""
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ]

def load_json(path):
    """Load a JSON file and return the data."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    """Save data to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def log_step(message):
    """Print a formatted step log."""
    print(f"\n🛠️  {message}")
