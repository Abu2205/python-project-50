def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return value


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]
        property_path = f"{path}.{key}" if path else key

        if node_type == "nested":
            lines.append(format_plain(node["children"], property_path))
        elif node_type == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{property_path}' was added with value: {value}")
        elif node_type == "removed":
            lines.append(f"Property '{property_path}' was removed")
        elif node_type == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{
                    property_path
                    }' was updated. From {
                        old_value} to {
                        new_value}"
                    )

    return "\n".join(lines)