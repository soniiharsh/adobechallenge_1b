import os
import sys

# Ensure you can import from utils when running from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from validate_schema import validate_output

if __name__ == "__main__":
    output_path = "../test_data/sample_output.json"
    schema_path = "../challenge1b_output_schema.json"

    if not os.path.exists(output_path):
        print(f"❌ Output file not found at {output_path}")
    elif not os.path.exists(schema_path):
        print(f"❌ Schema file not found at {schema_path}")
    else:
        try:
            validate_output(output_path, schema_path)
        except Exception as e:
            print(f"❌ Validation failed: {e}")
