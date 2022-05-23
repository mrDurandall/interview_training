# Задание 2

# Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
# целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.


def is_number_fractional(number):

    if number % 1:
        print(f'Число {number} является дробным')
        # return number // 1 == number % 1          формально "числа" до и после запятой равны быть не могут,
        #                                           потому что до запятой у нас число больше единицы, а после - меньше
        #                                           Но, видимо, надо сравнить наборы цифр до и после запятой ;)
        return str(number).split('.')[0] ==str (number).split('.')[1]
    else:
        print(f'Число {number} является целым')


def main():

    print(is_number_fractional(6))
    print(is_number_fractional(3.14))
    print(is_number_fractional(5.5))
    print(is_number_fractional(int(input('Введите число: '))))


if __name__ == '__main__':
    main()
    