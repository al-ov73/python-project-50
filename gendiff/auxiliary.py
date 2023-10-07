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
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return data
