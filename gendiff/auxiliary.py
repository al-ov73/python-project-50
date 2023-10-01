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


def bul_to_str(data):
    result = {}
    for k, v in data.items():
        if isinstance(v, bool):
            v_new = str(v).lower()
            result[k] = v_new
        elif v is None:
            result[k] = 'null'
        elif isinstance(v, dict):
            result[k] = bul_to_str(v)
        else:
            result[k] = v
    return result


def data_from_file(path_to_file):
    lst = path_to_file.split('.')
    extension = lst[-1]
    if extension == 'json':
        return json.load(open(path_to_file))
    elif extension == 'yml' or extension == 'yaml':
        with open(path_to_file) as f:
            return yaml.load(f, Loader=Loader)
