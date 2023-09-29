import json
import yaml
from yaml import CLoader as Loader


def dict_to_str(dict):
    result = ''
    for k, v in dict.items():
        if not result:
            result += f'{k}: {v}'
        else:
            result += f'\n {k}: {v}'
    final = f'{{\n{result}\n}}'
    return final


def bul_to_str(dict):
    result = {}
    for k, v in dict.items():
        if isinstance(v, bool):
            dict[k] = str(v).lower()
    return result


def data_from_file(path_to_file):
    lst = path_to_file.split('.')
    extension = lst[-1]
    if extension == 'json':
        return json.load(open(path_to_file))
    elif extension == 'yml' or extension == 'yaml':
        with open(path_to_file) as f:
            return yaml.load(f, Loader=Loader)
