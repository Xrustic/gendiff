def print_diff(diff_tree: dict) -> str:
    result = '{\n'
    for key, value in diff_tree.items():
        if isinstance(value, dict):
            result[key] = print_diff(value)
        if 'value' in value:
            result += '  ' + value['type'] + ' ' + key + ': ' \
                + str(value['value']) + '\n'
        else:
            result += '  - ' + key + ': ' + str(value['old_value']) + '\n'
            result += '  + ' + key + ': ' + str(value['new_value']) + '\n'
    result += '}'
    result = result.lower()
    print(result)
    return result
