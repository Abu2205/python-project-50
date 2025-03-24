import json
import os

import yaml


def parse_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def parse_data(data, ext):
    if ext == ".json":
        return json.loads(data)
    elif ext in (".yaml", ".yml"):
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    
    
def load_data(file_path):
    ext = os.path.splitext(file_path)[1]
    raw_data = parse_file(file_path)
    return parse_data(raw_data, ext)