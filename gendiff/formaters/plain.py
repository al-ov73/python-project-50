def add_quotes(item):
    """
    Add '' to input items, if it not in noneed_list
    Output - string
    """
    noneed_list = [
        'true', 'false', 'None', 'null', '[complex value]',
        'added', 'deleted', 'changed', 'unchanged'
    ]
    if item not in noneed_list and not isinstance(item, int):
        return f"'{item}'"
    else:
        return item


def to_complex_value(data):
    """
    Convert input dictionary to '[complex value]'
    Other data doesn't convert
    """
    if isinstance(data, dict):
        return '[complex value]'
    else:
        return data


def del_empty_line(text, acc):
    """
    Delete empty line in the end of input text file
    Output - string
    """
    if not acc:
        return text[:text.rfind('\n')]
    else:
        return text


def format_to_plain(data, acc=''):
    """
    Format input dictionary to 'plain' style
    Output - string
    """
    result = ''
    current_acc = acc
    for k, v in data.items():
        acc = current_acc
        if v[0] == 'unchanged' and isinstance(v[1], dict):
            acc += f'{k}.'
            result += format_to_plain(v[1], acc)
        elif v[0] == 'added':
            acc += f'{k}'
            new_v = add_quotes(to_complex_value(v[1]))
            result += f"Property '{acc}' was added with value: {new_v}\n"
            acc = current_acc
        elif v[0] == 'deleted':
            acc += f'{k}'
            result += f"Property '{acc}' was removed\n"
            acc = current_acc
        elif v[0] == 'changed':
            acc += f'{k}'
            n_v1 = add_quotes(to_complex_value(v[1]))
            n_v2 = add_quotes(to_complex_value(v[2]))
            result += f"Property '{acc}' was updated. From {n_v1} to {n_v2}\n"
            acc = current_acc
    return del_empty_line(result, current_acc)
