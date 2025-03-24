from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name):
    if format_name == "stylish":
        return format_stylish
    if format_name == "plain":
        return format_plain
    if format_name == "json":
        return format_json
    raise ValueError(f"Unknown format: {format_name}")


def apply_formatter(diff_tree, format_name):
    formatter = get_formatter(format_name)

    if format_name == "stylish":
        return f"{{\n{formatter(diff_tree)}\n}}"

    return formatter(diff_tree)