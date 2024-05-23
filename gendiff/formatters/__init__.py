from .stylish_format import stylish
from .plain_format import plain
from .json_format import json_form


def format(diff_tree, formatter):
    match formatter:
        case 'stylish':
            print(stylish(diff_tree))
            return stylish(diff_tree)
        case 'plain':
            print(plain(diff_tree))
            return plain(diff_tree)
        case 'json':
            print(json_form(diff_tree))
            return json_form(diff_tree)
        # case _:
        #     ValueError(f'Unsupported format: {formatter}')
