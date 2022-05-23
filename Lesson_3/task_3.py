# Задание 3

# Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь.
# Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
# Если есть значения, которым не хватило ключей, их необходимо отбросить.


def create_dictionary(keys, values):
    if not (isinstance(keys, list) or isinstance(values, list)):
        raise ValueError
    result_dict = {}

    for position in range(len(keys)):
        if position <= len(values) - 1:
            result_dict[keys[position]] = values[position]
        else:
            result_dict[keys[position]] = None

    return result_dict


def main():

    keys_1 = [1, 2, 3, 4, 5]
    values_1 = [1, 2, 3, 4, 5]
    dict_1 = create_dictionary(keys_1, values_1)
    print(dict_1)

    keys_2 = [1, 2, 3, ]
    values_2 = [1, 2, 3, 4, 5]
    dict_2 = create_dictionary(keys_2, values_2)
    print(dict_2)

    keys_2 = [1, 2, 3, 4, 5]
    values_2 = [1, 2, 3, ]
    dict_2 = create_dictionary(keys_2, values_2)
    print(dict_2)


if __name__ == '__main__':
    main()
    