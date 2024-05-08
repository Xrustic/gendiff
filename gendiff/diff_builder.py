from .consts import NESTED, DELETED, ADDED, UNCHANGED, CHANGED
from .parser import parse_data
from .gendiff import get_extension
from .formatters.stylish import stylish
from .formatters.plain import plain
from .formatters.json import json


def generate_diff(path1, path2, format):
    if isinstance(path1, dict) and isinstance(path2, dict):
        file1 = path1
        file2 = path2
    else:
        file1 = get_file_data(path1)
        file2 = get_file_data(path2)
    diff_tree = create_diff_tree(file1, file2)
# удалить принты
    if format == 'stylish':
        print(stylish(diff_tree))
        return stylish(diff_tree)
    elif format == 'plain':
        print(plain(diff_tree))
        return plain(diff_tree)
    else:
        print(json(diff_tree))
        return json(diff_tree)


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


def get_file_data(file_path):
    file_extension = get_extension(file_path)
    with open(file_path) as file:
        return parse_data(file, file_extension)
