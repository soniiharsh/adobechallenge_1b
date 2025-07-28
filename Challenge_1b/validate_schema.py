import jsonschema
import json

def validate_output(output_path, schema_path):
    with open(output_path) as f:
        data = json.load(f)
    with open(schema_path) as f:
        schema = json.load(f)
    jsonschema.validate(instance=data, schema=schema)
    print("✅ Output validated successfully.")
