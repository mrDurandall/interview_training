# Задание 2

# 2. Реализовать функцию print_directory_contents(path). Функция принимает имя
# директории и выводит ее содержимое, включая содержимое всех
# поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя,
# но можно использовать os.listdir и os.path.isfile

import os


def print_directory_contents(path):

    for elem in os.listdir(path):
        if os.path.isfile(f'{path}\\{elem}'):
            print(path.split('\\')[-1], '-', elem)
        else:
            print(path.split('\\')[-1], '-', elem, ':')
            print_directory_contents(f'{path}\\{elem}')


def main():

    directory_path = input('Введите путь к папке: ')
    try:
        print_directory_contents(directory_path)
    except NotADirectoryError:
        print('Указанный объект не является папкой!')
    except FileNotFoundError:
        print('Указан некорректный путь!')


if __name__ == '__main__':

    main()
