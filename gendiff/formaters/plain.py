def add_quotes(data):
    bool_list = ['true', 'false', 'None', 'null']
    prop_list = ['added', 'deleted', 'changed', 'unchanged']
    for k, v in data.items():
        new_v = []
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    new_item = add_quotes(item)
                    new_v.append(item)
                elif item not in prop_list and item not in bool_list and not isinstance(item, int):
                    new_item = (f"'{item}'")
                    new_v.append(new_item)
                else:
                    new_v.append(item)
            data[k] = new_v
    return data


def plain(data, acc=''):
    if acc == '':
        add_quotes(data)  # Добавляем ковычки для не int и не bool
    result = ''
    current_acc = acc
    for k, v in data.items():
        acc = current_acc
        if v[0] == 'added':
            acc += f'{k}'
            if isinstance(v[1], dict):
                v[1] = '[complex value]'
            result += f"Property '{acc}' was added with value: {v[1]}\n"
            acc = current_acc
        elif v[0] == 'deleted':
            acc += f'{k}'
            if isinstance(v[1], dict):
                v[1] = '[complex value]'
            result += f"Property '{acc}' was removed\n"
            acc = current_acc
        elif v[0] == 'changed':
            acc += f'{k}'
            if isinstance(v[1], dict):
                v[1] = '[complex value]'
            result += f"Property '{acc}' was updated. From {v[1]} to {v[2]}\n"
            acc = current_acc
        elif v[0] == 'unchanged' and isinstance(v[1], dict):
            acc += f'{k}.'
            result += plain(v[1], acc)
    return result
