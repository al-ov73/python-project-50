def stylish(data, replacer=' ', spaces_count=4, depth=1):
    result = ''
    depth_prev = depth
    for k, v in data.items():
        # Если значение изменилось
        if isinstance(v, list):
            # Проверяются значения по промежуточным тегам
            # 'added' 'deleted' 'unchanged' 'changed'
            # Внутри проверка, является ли значение словарем,
            # тогда проваливаемся глубже
            if v[0] == 'added':
                if isinstance(v[1], dict):
                    result += f'{replacer*(spaces_count*depth-2)}+ {k}: {{\n'
                    # Переменная, чтобы при проваливании внутрь,
                    # depth передавался след значениям бе изменений
                    new_depth = depth + 1
                    result += f'{stylish(v[1], replacer, spaces_count, new_depth)}\n'
                else:
                    result += f'{replacer*(spaces_count*depth_prev-2)}+ {k}: {v[1]}\n'
            elif v[0] == 'deleted':
                if isinstance(v[1], dict):
                    result += f'{replacer*(spaces_count*depth-2)}- {k}: {{\n'
                    new_depth = depth + 1
                    result += f'{stylish(v[1], replacer, spaces_count, new_depth)}\n'
                else:
                    result += f'{replacer*(spaces_count*depth_prev-2)}- {k}: {v[1]}\n'
            elif v[0] == 'unchanged':
                if isinstance(v[1], dict):
                    result += f'{replacer*(spaces_count*depth-2)}  {k}: {{\n'
                    new_depth = depth + 1
                    result += f'{stylish(v[1], replacer, spaces_count, new_depth)}\n'
                else:
                    result += f'{replacer*(spaces_count*depth_prev-2)}  {k}: {v[1]}\n'
            elif v[0] == 'changed':
                result += f'{replacer*(spaces_count*depth_prev-2)}- {k}: {v[1]}\n'
                result += f'{replacer*(spaces_count*depth_prev-2)}+ {k}: {v[2]}\n'
        # Если значение - словарь без изменений
        elif isinstance(v, dict):
            result += f'{replacer*(spaces_count*depth-2)}  {k}: {{\n'
            new_depth = depth + 1
            result += f'{stylish(v, replacer, spaces_count, new_depth)}\n'
        # Если значение - не словарь и не изменился
        else:
            result += f'{replacer*(spaces_count*depth-2)}  {k}: {v}\n'
    # Проверка для вывода самой первой фигурной скобки
    if depth_prev == 1:
        final = f'{{\n{result}{replacer*(spaces_count*depth_prev-4)}}}'
    else:
        final = f'{result}{replacer*(spaces_count*depth_prev-4)}}}'
    return final
