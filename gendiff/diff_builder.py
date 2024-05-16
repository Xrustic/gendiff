from .consts import NESTED, DELETED, ADDED, UNCHANGED, CHANGED


def create_diff_tree(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[key] = {'type': DELETED, 'value': file1[key]}
        elif key not in file1:
            result[key] = {'type': ADDED, 'value': file2[key]}

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = {
                "type": NESTED,
                "value": create_diff_tree(file1[key], file2[key]),
            }
        elif file1[key] != file2[key]:
            result[key] = {
                "type": CHANGED,
                "old_value": file1[key],
                "new_value": file2[key]
            }
        else:
            result[key] = {'type': UNCHANGED, 'value': file1[key]}
    return result
