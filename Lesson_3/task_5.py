# Задание 5

# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
# (выбирается случайно) заменить на значения типа 345example (в обратном порядке, число и строка).
# Реализовать функцию поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.

import os, sys
from random import randint


def random_text_generator():

    letters_list = [chr(randint(97, 122)) for _ in range(randint(5, 10))]
    return ''.join(letters_list)


def create_file(filename):

    file_path = os.path.join(os.getcwd(), filename)
    if os.path.isfile(file_path):
        raise FileExistsError
    with open(filename, 'w', encoding='utf-8') as file:
        numbers = [randint(1, 100) for _ in range(10)]
        texts = [random_text_generator() for _ in range(10)]
        for number, text in zip(numbers, texts):
            if randint(0, 1):
                file.write(f'{text}{number}\n')
            else:
                file.write(f'{number}{text}\n')


def read_file(filename):

    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        raise FileExistsError
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


def find_substring(filename, substring):

    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        raise FileExistsError
    with open(filename, 'r', encoding='utf-8') as file:
        print(f'Строки, в которые входит подстрока {substring}')
        for line_number, line in enumerate(file):
            if line.count(substring):
                print(f'{line_number}:   {line}', end='')


def change_substring(filename, substring, new_substring):

    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        raise FileExistsError
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file):
            if line.count(substring):
                splitted_string = line.partition(substring)
                print(f'Подстрока {substring} найдена в строке №{line_number}:   {line}', end='')
                print(f'вид строки после замены: {splitted_string[0]}{new_substring}{splitted_string[2]}', end='')


def main():
    try:
        create_file('test.txt')
    except FileExistsError:
        print('Файл с таким именем уже существует')
        sys.exit()

    try:
        read_file('test.txt')
    except FileExistsError:
        print('Файл с таким именем не существует')
        sys.exit()

    find_substring('test.txt', input('Введите подстроку для поиска: '))
    change_substring('test.txt', input('Введите что заменяем: '), input('Ввдеите на что заменяем: '))


if __name__ == '__main__':
    main()
    