import os
from gendiff import generate_diff

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def test_generate_diff_plain():
    file1 = os.path.join(BASE_DIR, "test_data", "file1.json")
    file2 = os.path.join(BASE_DIR, "test_data", "file2.json")
    
    diff = generate_diff(file1, file2, 'plain')
    expected = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

    assert diff == expected