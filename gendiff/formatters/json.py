import json
import gendiff.consts


def json_form(data):
    for value in data.values():
        match value['type']:
            case gendiff.consts.DELETED:
                value['type'] = '-'
            case gendiff.consts.ADDED:
                value['type'] = '+'
            case gendiff.consts.CHANGED:
                value['type'] = '-+'
            case gendiff.consts.UNCHANGED:
                value['type'] = ' '
    return json.dumps(data)
