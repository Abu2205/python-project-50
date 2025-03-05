from gendiff import generate_diff
import os


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected_result.txt'))
    assert generate_diff(file1, file2) == expected