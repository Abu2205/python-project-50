from gendiff.diff_builder import build_diff
from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parser import parse_file


def generate_diff(file1, file2, format_name):
    
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return f"{{\n{format_stylish(diff_tree)}\n}}"
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f"Unknown format: {format_name}")