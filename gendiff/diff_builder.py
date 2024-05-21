from .consts import TYPES


def create_diff_tree(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[key] = {'type': TYPES.DELETED, 'value': file1[key]}
        elif key not in file1:
            result[key] = {'type': TYPES.ADDED, 'value': file2[key]}

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = {
                "type": TYPES.NESTED,
                "value": create_diff_tree(file1[key], file2[key]),
            }
        elif file1[key] != file2[key]:
            result[key] = {
                "type": TYPES.CHANGED,
                "old_value": file1[key],
                "new_value": file2[key]
            }
        else:
            result[key] = {'type': TYPES.UNCHANGED, 'value': file1[key]}
    return result
