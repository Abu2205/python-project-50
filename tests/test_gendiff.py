from gendiff import generate_diff
import os


def get_fixture_path(filename):
    return os.path.join('tests', 'test_data', filename)


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected_result.txt'))
    assert generate_diff(file1, file2) == expected

def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yaml')
    expected_result = read_file(get_fixture_path('expected_results.txt'))
    assert generate_diff(file1, file2) == expected_result