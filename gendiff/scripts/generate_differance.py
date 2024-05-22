#!/usr/bin/env python3
from gendiff.cli import parser
from gendiff.gendiff import gen_diff


def main():
    args = parser()
    return gen_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
