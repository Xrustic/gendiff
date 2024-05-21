from collections import namedtuple


INDENT = '    '
_TYPE_VALUES = ('deleted', 'added', 'nested', 'changed', 'unchanged')
TYPES = namedtuple('FormatTypes',
                   map(str.upper, _TYPE_VALUES))(*_TYPE_VALUES)
_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple('FormatChoices',
                     map(str.upper, _FORMAT_VALUES))(*_FORMAT_VALUES)
