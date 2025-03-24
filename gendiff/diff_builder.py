def build_diff(data1, data2):
    diff = []
    keys = sorted(set(data1) | set(data2))

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key in data2 and isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({"key": key, "type": "nested", "children": build_diff(value1, value2)})
        elif key in data1 and key in data2 and value1 == value2:
            diff.append({"key": key, "type": "unchanged", "value": value1})
        elif key in data1 and key in data2:
            diff.append({"key": key, "type": "changed", "old_value": value1, "new_value": value2})
        elif key in data1:
            diff.append({"key": key, "type": "removed", "value": value1})
        else:
            diff.append({"key": key, "type": "added", "value": value2})

    return diff