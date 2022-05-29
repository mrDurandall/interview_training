# Задание 1

# 1. Вывести таблицу умножения в виде.
# 1 x 1 = 1
# 1 x 2 = 2
# ..
# 1 x 10 = 10
# —
# 2 x 1 = 2
# 2 x 2 = 4
# …
# N x 10 = 10N
# Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
# Между разделами вывести разделитель в виде 5 девисов


def print_multiplication_table(last_number):
    if last_number < 1:
        raise ValueError
    for first_multiplier in range(1, last_number+1):
        for second_multiplier in range(1, 11):
            print(f'{first_multiplier} x {second_multiplier} = {first_multiplier * second_multiplier}')
        if first_multiplier != last_number:
            print('-----')


def main():
    try:
        print_multiplication_table(int(input('Введите последний множитель таблицы: ')))
    except ValueError:
        print('Ошибка! Введенное значение должно быть целым положительным числом!')


if __name__ == '__main__':
    main()
