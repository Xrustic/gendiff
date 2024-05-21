from .stylish_format import stylish
from .plain_format import plain
from .json_format import json_form


def format(diff_tree, formatter):
    if formatter == 'stylish':
        print(stylish(diff_tree))
        return stylish(diff_tree)
    elif formatter == 'plain':
        print(plain(diff_tree))
        return plain(diff_tree)
    else:
        print(json_form(diff_tree))
        return json_form(diff_tree)
