def format_value(value, depth):
    if isinstance(value, dict):
        indent = " " * ((depth + 1) * 4)
        lines = [f"{indent}{key}: {format_value(val, depth + 1)}" for key,
                  val in value.items()]
        return "{{\n{}\n{}}}".format("\n".join(lines), " " * (depth * 4))
    return stringify(value)


def stringify(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff_tree, depth=1):
    indent = " " * (depth * 4 - 2)
    lines = []

    for node in diff_tree:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")
        elif node_type == "added":
            lines.append(f"{indent}+ {key}: {format_value(node['value'],
                                                           depth)}")
        elif node_type == "removed":
            lines.append(f"{indent}- {key}: {format_value(node['value'],
                                                           depth)}")
        elif node_type == "unchanged":
            lines.append(f"{indent}  {key}: {format_value(node['value'],
                                                           depth)}")
        elif node_type == "changed":
            lines.append(f"{indent}- {key}: {format_value(node['old_value'],
                                                           depth)}")
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'],
                                                           depth)}")

    result = "\n".join(lines)
    return f"{{\n{result}\n}}" if depth == 1 else result