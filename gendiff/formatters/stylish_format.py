import gendiff.consts


def build_indent(depth):
    return gendiff.consts.INDENT[:-2] + gendiff.consts.INDENT * depth


def format_data_to_stylish(data, depth):
    string_data = '\n'.join(data)
    last_indent = build_indent(depth)[:-2]
    return f'{string_data}\n{last_indent}'


def put_into_braces(formatted_data):
    return f'{{\n{formatted_data}}}'


def to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'{build_indent(depth)}  '
                         f'{key}: {to_str(val, depth + 1)}')
        lines_string = format_data_to_stylish(lines, depth)
        return put_into_braces(lines_string)
    return value


def stylish(data):
    def _it_stylish(data, depth=0):
        result = []
        for key, value in data.items():
            match value['type']:
                case gendiff.consts.DELETED:
                    result.append(f'{build_indent(depth)}- {key}: '
                                  f'{to_str(value["value"], depth + 1)}')
                case gendiff.consts.ADDED:
                    result.append(f'{build_indent(depth)}+ {key}: '
                                  f'{to_str(value["value"], depth + 1)}')
                case gendiff.consts.CHANGED:
                    result.append(f'{build_indent(depth)}- {key}: '
                                  f'{to_str(value["old_value"], depth + 1)}')
                    result.append(f'{build_indent(depth)}+ {key}: '
                                  f'{to_str(value["new_value"], depth + 1)}')
                case gendiff.consts.UNCHANGED:
                    result.append(f'{build_indent(depth)}  {key}: '
                                  f'{to_str(value["value"], depth + 1)}')
                case gendiff.consts.NESTED:
                    result.append(f'{build_indent(depth)}  {key}: '
                                  f'{_it_stylish(value["value"], depth + 1)}')
                case _:
                    raise ValueError(f'Unknown type: {value["type"]}')

        result_string = format_data_to_stylish(result, depth)
        return put_into_braces(result_string)

    return _it_stylish(data)
