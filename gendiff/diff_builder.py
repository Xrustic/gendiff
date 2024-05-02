from .parser import parse_data
from .consts import NESTED, DELETED, ADDED, UNCHANGED, CHANGED
import os


def create_difference_tree(path1, path2):
    if isinstance(path1, dict) and isinstance(path2, dict):
        file1 = path1
        file2 = path2
    else:
        file1 = get_file_data(path1)
        file2 = get_file_data(path2)

    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[key] = {'type': DELETED, 'value': file1[key]}
        elif key not in file1:
            result[key] = {'type': ADDED, 'value': file2[key]}
        elif file1[key] == file2[key]:
            result[key] = {'type': UNCHANGED, 'value': file1[key]}

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = {
                "type": NESTED,
                "value": create_difference_tree(file1[key], file2[key]),
            }
        elif file1[key] != file2[key]:
            result[key] = {
                "type": CHANGED,
                "old_value": file1[key],
                "new_value": file2[key]
            }
    return result


def get_file_data(file_path):
    file_extension = get_extension(file_path)
    with open(file_path) as file:
        return parse_data(file, file_extension)


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]
