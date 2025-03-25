def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = " " * (depth * 4)
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {
                format_value(val, depth + 1)}")
        return "{{\n{}\n{}}}".format("\n".join(lines), indent)
    return stringify(value)


def stringify(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff_tree, depth=0):
    indent = " " * (depth * 4)
    lines = []
    for node in diff_tree:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}    {key}: {{\n{children}\n{indent}    }}")
        elif node_type == "added":
            lines.append(f"{indent}  + {key}: {
                format_value(node['value'], depth + 1)}")
        elif node_type == "removed":
            lines.append(f"{indent}  - {key}: {
                format_value(node['value'], depth + 1)}")
        elif node_type == "unchanged":
            lines.append(f"{indent}    {key}: {
                format_value(node['value'], depth + 1)}")
        elif node_type == "changed":
            lines.append(
                f"{indent}  - {key}: {
                    format_value(node['old_value'], depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}: {
                    format_value(node['new_value'], depth + 1)}"
            )
    formatted_diff = "\n".join(lines)
    return f"{{\n{formatted_diff}\n{indent}}}"