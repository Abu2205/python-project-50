import json

from gendiff import generate_diff


def test_generate_diff_json():
    file1 = "tests/test_data/file1.json"
    file2 = "tests/test_data/file2.json"
    diff = generate_diff(file1, file2, format_name="json")
    parsed = json.loads(diff)
    assert isinstance(parsed, list)
