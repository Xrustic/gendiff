from .consts import NESTED, DELETED, ADDED, UNCHANGED, CHANGED
from .parser import parse_data
from .gendiff import get_extension
from .formatters.stylish import stylish


def get_file_data(file_path):
    file_extension = get_extension(file_path)
    with open(file_path) as file:
        return parse_data(file, file_extension)


def generate_diff(path1, path2):
    diff_tree = create_difference_tree(path1, path2)
    print(stylish(diff_tree))
    return stylish(diff_tree)


def create_difference_tree(path1, path2):
    file1 = get_file_data(path1)
    file2 = get_file_data(path2)

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
                "value": create_difference_tree(file1[key], file2[key]),
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
