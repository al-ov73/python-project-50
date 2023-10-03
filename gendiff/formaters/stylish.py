def make_symbol(text):
    if text == 'added':
        return '+ '
    if text == 'deleted':
        return '- '
    if text == 'unchanged':
        return '  '


def add_bracket(result, replacer, spaces_count, depth_prev, acc):
    if acc == 1:
        return f'{{\n{result}{replacer*(spaces_count*depth_prev-4)}}}'
    return f'{result}{replacer*(spaces_count*depth_prev-4)}}}'


def make_change(k, v, result, replacer, spaces_count, depth):
    if isinstance(v, list) and v[0] == 'changed' and isinstance(v[1], dict):
        result += f'{replacer*(spaces_count*depth-2)}- {k}: {{\n'
        new_depth = depth + 1
        result += (
            f'{format_stylish(v[1], replacer, spaces_count, new_depth)}\n'
        )
        result += f'{replacer*(spaces_count*depth-2)}+ {k}: {v[2]}\n'
    elif isinstance(v, list) and v[0] == 'changed' and isinstance(v[2], dict):
        result += f'{replacer*(spaces_count*depth-2)}- {k}: {v[1]}\n'
        result += f'{replacer*(spaces_count*depth-2)}+ {k}: {{\n'
        new_depth = depth + 1
        result += (
            f'{format_stylish(v[2], replacer, spaces_count, new_depth)}\n'
        )
    elif (isinstance(v, list) and v[0] == 'changed' and
            not isinstance(v[1], dict) and not isinstance(v[2], dict)):
        result += f'{replacer*(spaces_count*depth-2)}- {k}: {v[1]}\n'
        result += f'{replacer*(spaces_count*depth-2)}+ {k}: {v[2]}\n'
    return result


def format_stylish(data, replacer=' ', spaces_count=4, depth=1):
    result = ''
    depth_prev = depth
    for k, v in data.items():
        # Если значение изменилось
        if (isinstance(v, list) and (
            v[0] == 'added' or v[0] == 'deleted' or v[0] == 'unchanged')
                and isinstance(v[1], dict)):
            result += (
                f'{replacer*(spaces_count*depth-2)}{make_symbol(v[0])}{k}: {{\n'
            )
            new_depth = depth + 1
            result += (
                f'{format_stylish(v[1], replacer, spaces_count, new_depth)}\n'
            )
        elif (isinstance(v, list) and
                (v[0] == 'added' or v[0] == 'deleted' or v[0] == 'unchanged')):
            result += (
                f'{replacer*(spaces_count*depth_prev-2)}'
                f'{make_symbol(v[0])}{k}: {v[1]}\n'
            )
        elif isinstance(v, list) and v[0] == 'changed':
            result = make_change(k, v, result, replacer, spaces_count, depth)
        # Если значение - словарь без изменений
        elif isinstance(v, dict):
            result += f'{replacer*(spaces_count*depth-2)}  {k}: {{\n'
            new_depth = depth + 1
            result += (
                f'{format_stylish(v, replacer, spaces_count, new_depth)}\n'
            )
        # Если значение - не словарь и не изменился
        else:
            result += f'{replacer*(spaces_count*depth-2)}  {k}: {v}\n'
    return add_bracket(result, replacer, spaces_count, depth_prev, depth_prev)
