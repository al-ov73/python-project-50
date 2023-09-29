from gendiff.auxiliary import bul_to_str, dict_to_str, data_from_file


def generate_diff(first_file, second_file):
    data1 = data_from_file(first_file)
    data2 = data_from_file(second_file)
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
