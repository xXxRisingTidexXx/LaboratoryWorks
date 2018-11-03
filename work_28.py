"""
Лабораторна робота №28
ІПЗ - 12, Петраківський Данило
"""
from os import stat
from re import match


def output_properties():
    """
    #1
    """
    props = properties(input('Введіть ім\'я файлу: '))
    print('Ім\'я: {}'.format(props[0]))
    print('Розширення: {}'.format(props[1]))
    print('Тип: {}'.format(props[2]))
    print('Дата останнього редагування: {}'.format(props[3]))
    print('Атрибути: {}'.format(props[4]))


def properties(filename):
    state = stat(filename)
    return filename, match(r'\S+(\.\w+)$', filename).groups()[0], 'file', state.st_mtime, state.st_size


def output_row_count():
    """
    #2
    """
    for i in range(3):
        print('Кількість рядків: {}'.format(row_count(input('Введіть ім\'я файлу: '))))


def row_count(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 1


def numerate_rows():
    """
    #3
    """


def create_files():
    """
    #4
    """


def text_to_binary():
    """
    #5
    """


def caesar_cipher():
    """
    #6
    """
