import json
import yaml


def parse_data(data, extension):
    match extension:
        case 'json':
            return json.load(data)
        case 'yml' | 'yaml':
            return yaml.safe_load(data)

    ValueError(f'Unsupported extension: {extension}')
