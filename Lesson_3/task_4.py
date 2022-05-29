# Задание 4

# Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
# Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
# Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
# Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.

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
            file.write(f'{text}{number}\n')


def read_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        raise FileExistsError
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


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


if __name__ == '__main__':
    main()
    