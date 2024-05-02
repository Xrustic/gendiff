#!/usr/bin/env python3
import argparse
from .diff_builder import create_difference_tree
from .formatters.stylish import stylish


def generate_diff(path1, path2):
    diff_tree = create_difference_tree(path1, path2)
    return stylish(diff_tree)


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
