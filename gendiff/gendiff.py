import json


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


def generate_diff(first_file, second_file):
    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))
    result = {}
    for k in sorted(data1 | data2):
        if data1.get(k) == data2.get(k):
            result[k] = data1.get(k)
        elif k in data1 and k not in data2:
            new_k = f'- {k}'
            result[new_k] = data1.get(k)
        elif k in data1 and k in data2 and data1.get(k) != data2.get(k):
            new_k = f'- {k}'
            result[new_k] = data1.get(k)
            new_k_2 = f'+ {k}'
            result[new_k_2] = data2.get(k)
        elif k in data2 and k not in data1:
            new_k = f'+ {k}'
            result[new_k] = data2.get(k)
    bul_to_str(result)
    return dict_to_str(result)
