from gendiff.auxiliary import bul_to_str, data_from_file


def generate_diff(first_file, second_file):
    data1 = bul_to_str(data_from_file(first_file))
    data2 = bul_to_str(data_from_file(second_file))

    def generate_diff_dict(dict1, dict2):
        result = {}
        keys = dict1.keys() | dict2.keys()
        for key in sorted(keys):
            if key not in dict1:
                result[key] = ['added', dict2[key]]
            elif key not in dict2:
                result[key] = ['deleted', dict1[key]]
            elif dict1[key] == dict2[key]:
                result[key] = ['unchanged', dict1[key]]
            # ключи равны, значения отличаются
            elif key in dict1 and key in dict2 and dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    children1 = dict1[key]
                    children2 = dict2[key]
                    new_value = generate_diff_dict(children1, children2)
                    result[key] = ['unchanged', new_value]
                else:
                    result[key] = ['changed', dict1[key], dict2[key]]
        return result
    return generate_diff_dict(data1, data2)
