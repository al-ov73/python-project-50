from gendiff.auxiliary import bul_to_str, data_from_file
from gendiff.formaters import stylish, plain, json


def generate_diff_dict(dict1, dict2):
    """
    Return intermediary dictionary {key: ['added/deleted/...', value]}
    Output - dictionary
    """
    result = {}
    keys = dict1.keys() | dict2.keys()
    for key in sorted(keys):
        if key not in dict1:
            result[key] = ['added', dict2[key]]
        elif key not in dict2:
            result[key] = ['deleted', dict1[key]]
        elif dict1[key] == dict2[key]:
            result[key] = ['unchanged', dict1[key]]
        elif (dict1[key] != dict2[key] and
              isinstance(dict1[key], dict) and
              isinstance(dict2[key], dict)):
            # ключи равны, значения отличаются и они - словари
            children1 = dict1[key]
            children2 = dict2[key]
            new_value = generate_diff_dict(children1, children2)
            result[key] = ['unchanged', new_value]
        else:
            result[key] = ['changed', dict1[key], dict2[key]]
    return result


def generate_diff(first_file, second_file, format_name='stylish'):
    """
    Return dictionary, formated depends on 'format_name'
    format_name:'stylish'(default), 'plain', 'json'
    Output - dictionary
    """
    data1 = bul_to_str(data_from_file(first_file))  # -> dict
    data2 = bul_to_str(data_from_file(second_file))  # -> dict
    # Промежуточный словарь
    inter_dict = generate_diff_dict(data1, data2)
    if format_name == 'stylish':
        return stylish.format_stylish(inter_dict)
    elif format_name == 'plain':
        return plain.format_to_plain(inter_dict)
    elif format_name == 'json':
        return json.format_to_json(inter_dict)
