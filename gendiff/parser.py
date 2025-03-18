import json
import os

import yaml


def parse_file(file_path):
    ext = os.path.splitext(file_path)[1]
    with open(file_path) as file:
        if ext in [".json"]:
            return json.load(file)
        elif ext in [".yaml", ".yml"]:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
