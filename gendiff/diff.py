import os

from gendiff.diff_builder import build_diff
from gendiff.file_parser import parse_data, parse_file
from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def generate_diff(file1, file2, format_name="stylish"):
    raw_data1 = parse_file(file1)
    raw_data2 = parse_file(file2)

    ext1 = os.path.splitext(file1)[1]
    ext2 = os.path.splitext(file2)[1]

    data1 = parse_data(raw_data1, ext1)
    data2 = parse_data(raw_data2, ext2)

    diff_tree = build_diff(data1, data2)

    formatters = {
        "stylish": lambda tree: f"{{\n{format_stylish(tree)}\n}}",
        "plain": format_plain,
        "json": format_json,
    }

    if format_name not in formatters:
        raise ValueError(f"Unknown format: {format_name}")

    return formatters[format_name](diff_tree)