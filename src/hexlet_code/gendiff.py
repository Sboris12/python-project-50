import json


def generate_diff(path1, path2):
    with open(path1) as file1, open(path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    keys = sorted(set(data1) | set(data2))
    lines = ["{"]

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {format_value(data1[key])}")
            else:
                lines.append(f"  - {key}: {format_value(data1[key])}")
                lines.append(f"  + {key}: {format_value(data2[key])}")
        elif key in data1:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  + {key}: {format_value(data2[key])}")

    lines.append("}")
    return "\n".join(lines)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value
