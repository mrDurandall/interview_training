# 3. Разработать целочисленный генератор случайных чисел. В функцию
# передавать начальную и конечную границу диапазона генерации (выдавать
# значения из диапазона включая концы). Заполнить этими данными словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”, а
# значене сгенеренное случайное число. Вывести содержимое словаря.
# (Усложненный вариант по желанию*): Не использовать стандартный модуль
# python random.

# Вариант без использования стандартного модуля random

# Работает довольно долго и случайность не слишком адкватна, но что-то похожее получается :)

import time
import sys


def custom_random_generator(lower_limit, upper_limit):
    now = time.time()
    # Без sleep цикл отрабатывал слишком быстро и получалось везде одно и то же значение
    time.sleep(now % 1)
    return int(round(lower_limit + (upper_limit - lower_limit) * (now % 1)))


def main():

    try:
        lower_limit = int(input('Введите нижнюю границу случайного числа: '))
    except ValueError:
        print('Введено некорректное значение!')
        sys.exit()
    try:
        upper_limit = int(input('Введите верхнюю границу случайного числа: '))
    except ValueError:
        print('Введено некорректное значение!')
        sys.exit()
    random_dict = {f'elem_{num+1}': custom_random_generator(lower_limit, upper_limit) for num in range(10)}
    print(random_dict)


if __name__ == '__main__':
    main()
