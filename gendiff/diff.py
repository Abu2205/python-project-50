from gendiff.diff_builder import build_diff
from gendiff.file_parser import load_data
from gendiff.formatters import apply_formatter


def generate_diff(file1, file2, format_name="stylish"):
    data1 = load_data(file1)
    data2 = load_data(file2)

    diff_tree = build_diff(data1, data2)

    return apply_formatter(diff_tree, format_name)