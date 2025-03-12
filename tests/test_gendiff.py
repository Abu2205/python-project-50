import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def read_fixture(filename):
    with open(get_fixture_path(filename)) as file:
        return file.read()


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_result = read_fixture('expected_result.txt')
    assert generate_diff(file1, file2, 'stylish') == expected_result


def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yaml')
    expected_result = read_fixture('expected_result.txt')
    assert generate_diff(file1, file2, 'stylish') == expected_result


def test_generate_diff_json_stylish():
    file1 = get_fixture_path('test_file1.json')
    file2 = get_fixture_path('test_file2.json')
    expected_result = read_fixture('expected_stylish_result.txt')
    assert generate_diff(file1, file2, format_name='stylish') == expected_result


def test_generate_diff_yaml_stylish():
    file1 = get_fixture_path('test_file1.yaml')
    file2 = get_fixture_path('test_file2.yaml')
    expected_result = read_fixture('expected_stylish_result.txt')
    assert generate_diff(file1, file2, format_name='stylish') == expected_result