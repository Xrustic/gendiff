#!/usr/bin/env python3
import argparse
import os
from .parser import parse_data


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def get_file_data(file_path):
    with open(file_path) as file:
        return parse_data(file, get_extension(file_path))


def generate_diff(path1, path2):
    diff_tree = create_difference_tree(path1, path2)
    return str(print_diff(diff_tree))


def print_diff(diff_tree: dict) -> str:
    result = '{\n'
    for key, value in diff_tree.items():
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


def create_difference_tree(path1, path2):
    file1 = get_file_data(path1)
    file2 = get_file_data(path2)
    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[key] = {'type': '-', 'value': file1[key]}
        elif key not in file1:
            result[key] = {'type': '+', 'value': file2[key]}
        elif file1[key] == file2[key]:
            result[key] = {'type': ' ', 'value': file1[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = {
                "type": "+",
                "value": create_difference_tree(file1[key], file2[key]),
            }
        else:
            result[key] = {
                "type": "-",
                "old_value": file1[key],
                "new_value": file2[key],
            }
    return result


def parser():
    parser = argparse.ArgumentParser(description='Compares two configuration\n'
                                     ' files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def main():
    parser()


if __name__ == '__main__':
    main()
