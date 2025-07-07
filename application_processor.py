import json

def process_application(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
