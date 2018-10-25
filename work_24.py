"""
Лабораторна робота №24
ІПЗ - 12, Петраківський Данило
"""
from re import compile

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def create_asterisk_file():
    """
    #1
    """
    filename = input('Введіть ім\'я файлу: ')
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    with open(filename, 'w') as file:
        file.write('\n'.join(['*' * k] * n))


def create_latin_letter_file():
    """
    #2
    """
    filename = input('Введіть ім\'я файлу: ')
    n = int(input('Введіть n: '))
    with open(filename, 'w') as file:
        file.write('\n'.join([alphabet[:i + 1] for i in range(n)]))


def create_mixed_file():
    """
    #3
    """
    filename = input('Введіть ім\'я файлу: ')
    n = int(input('Введіть n: '))
    with open(filename, 'w') as file:
        file.write('\n'.join([alphabet[:i + 1] + '*' * (n - i - 1) for i in range(n)]))


def get_char_and_line_count():
    """
    #4
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r') as file:
        char_count = 0
        lines = file.readlines()
        for line in lines:
            char_count += len(line)
        print('Кількість символів: %d, кількість рядків: %d' % (char_count, len(lines)))


def append_data():
    """
    #5
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'a') as file_1, open(filename_2, 'r') as file_2:
        file_1.write('\n' + file_2.read())


def push_data():
    """
    #6
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'r+') as file_1, open(filename_2, 'r') as file_2:
        lines = file_1.read()
        clear(file_1)
        file_1.write(file_2.read() + '\n' + lines)


def clear(file):
    file.seek(0)
    file.truncate()


def count_paragraphs():
    """
    #7
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r') as file:
        pattern = compile(r'^ {5}\S*')
        paragraph_count = 0
        for line in file.readlines():
            paragraph_count += 1 if pattern.match(line) else 0
        print('Кількість абзаців: %d' % paragraph_count)


def insert_empty_lines():
    """
    #8
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+') as file:
        lines = file.read().replace('     ', '\n     ')
        clear(file)
        file.write(lines[1:])
