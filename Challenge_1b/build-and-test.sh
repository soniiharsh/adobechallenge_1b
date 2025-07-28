#!/bin/bash

echo "🚀 Starting build and test pipeline..."

# Step 1: Install Python dependencies
echo "📦 Installing required Python packages..."
pip install -r requirements.txt

# Step 2: Run the main analysis script
echo "🧠 Running document analysis..."
python3 src/main.py

# Step 3: Validate the generated JSON output
echo "✅ Validating output schema..."
python3 utils/test_solution.py

echo "🎉 All steps completed."
