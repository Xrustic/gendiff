import os
from gendiff.parser import parse_data
from gendiff.formatters import format
from gendiff.diff_builder import create_diff_tree


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def generate_diff(path1, path2, formatters='stylish'):
    file1 = get_file_data(path1)
    file2 = get_file_data(path2)
    diff_tree = create_diff_tree(file1, file2)
    return format(diff_tree, formatters)


def get_file_data(file_path):
    file_extension = get_extension(file_path)
    with open(file_path) as file:
        return parse_data(file, file_extension)
