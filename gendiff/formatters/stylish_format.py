import gendiff.consts


def to_str(value, spaces_count=2):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = ' ' * (spaces_count + 4)
        lines = []
        for key, val in value.items():
            formatted_value = to_str(val, spaces_count + 4)
            lines.append(f'{indent}  {key}: {formatted_value}')
        formatted_string = '\n'.join(lines)
        end_indent = ' ' * (spaces_count + 2)
        return f'{{\n{formatted_string}\n{end_indent}}}    '
    else:
        return str(value)


def stylish(diff: dict):
    def _iter(diff: dict, spaces_count=2):
        lines = []
        for key, value in diff.items():
            indent = ' ' * spaces_count
            match value['type']:
                case gendiff.consts.UNCHANGED:
                    current_value = to_str(value['value'], spaces_count)
                    lines.append(f"{indent}  {key}: {current_value}")
                case gendiff.consts.DELETED:
                    current_value = to_str(value['value'], spaces_count)
                    lines.append(f"{indent}- {key}: {current_value}")
                case gendiff.consts.ADDED:
                    current_value = to_str(value['value'], spaces_count)
                    lines.append(f"{indent}+ {key}: {current_value}")
                case gendiff.consts.CHANGED:
                    current_value = to_str(value['old_value'], spaces_count)
                    lines.append(f"{indent}- {key}: {current_value}")

                    current_value = to_str(value['new_value'], spaces_count)
                    lines.append(f"{indent}+ {key}: {current_value}")
                case gendiff.consts.NESTED:
                    current_value = _iter(value['value'], spaces_count + 4)
                    lines.append(f"{indent}  {key}: {current_value}")
        formatted_string = '\n'.join(lines)
        end_indent = ' ' * (spaces_count - 2)
        return f'{{\n{formatted_string}\n{end_indent}}}'
    return _iter(diff)
