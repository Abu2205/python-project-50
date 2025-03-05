import json


def load_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    dict1 = load_json(file_path1)
    dict2 = load_json(file_path2)

    all_keys = sorted(set(dict1) | set(dict2))
    result = ['{']

    for key in all_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result.append(f'    {key}: {to_str(dict1[key])}')
            else:
                result.append(f'  - {key}: {to_str(dict1[key])}')
                result.append(f'  + {key}: {to_str(dict2[key])}')
        elif key in dict1:
            result.append(f'  - {key}: {to_str(dict1[key])}')
        else:  # key in dict2
            result.append(f'  + {key}: {to_str(dict2[key])}')

    result.append('}')
    return '\n'.join(result)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)
