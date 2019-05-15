"""
Лабораторна робота №28
ІПЗ - 12, Петраківський Данило
"""
from os import stat
from re import match


types = {'': 'binary', '.txt': 'text', '.pdf': 'text', '.doc': 'text', '.docx': 'text',
         '.mp3': 'audio', '.wav': 'audio', '.mp4': 'video', '.flv': 'video', '.ppt': 'presentations',
         '.pptx': 'presentations', '.xls': 'spreadsheets', '.xlsx': 'spreadsheets'}


def output_properties():
    """
    #1
    """
    props = properties(input('Введіть ім\'я файлу: '))
    print('Ім\'я: {}'.format(props[0]))
    print('Розширення: {}'.format(props[1]))
    print('Тип: {}'.format(props[2]))
    print('Дата останнього редагування: {}'.format(props[3]))
    print('Розмір: {}'.format(props[4]))


def properties(filename):
    state = stat(filename)
    extension = match(r'\S+(\.\w+)$', filename).groups()[0]
    return filename, extension, types[extension], state.st_mtime, state.st_size


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
    filename = input('Введіть ім\'я файлу: ')
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    m = int(input('Введіть m: '))
    with open(filename, 'r+') as file:
        lines = file.readlines()
        clear(file)
        for line in lines:
            file.write(expand(n, k, m, line))
            n += 1


def clear(file):
    file.seek(0)
    file.truncate()


def expand(n, k, m, line):
    return '{}{}{}{}'.format(' ' * (k - len(str(n))), n, ' ' * m if line != '\n' else '', line)


def create_files():
    """
    #4
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    k = int(input('Введіть k: '))
    with open(filename_1, 'r') as file_1, open(filename_2, 'w') as file_2, open(filename_3, 'w') as file_3:
        lines = file_1.readlines()
        for i in range(k):
            file_2.write(lines[i])
        for i in range(k, len(lines)):
            file_3.write(lines[i])


def text_file_to_binary_file():
    """
    #5
    """
    for i in range(2):
        text_to_binary(input('Введіть ім\'я {} файлу: '.format(i + 1)))


def text_to_binary(filename):
    with open(filename, 'r') as text_file, open(filename.partition('.')[0], 'wb') as binary_file:
        binary_file.write(bytes((text_file.read().encode('utf-8'))))


def caesar_cipher():
    """
    #6
    """
    filename = input('Введіть ім\'я файлу: ')
    k = int(input('Введіть k: '))
    with open(filename, 'r+') as file:
        text = file.read()
        print(text)
        clear(file)
        file.write(''.join([chshift(ch, k) if ch.isalpha() else ch for ch in text]))


def chshift(ch, shift):
    encr = ord(ch) + shift
    return (chr(encr) if encr <= 90 else chr(encr - 26)) if ch.isupper() \
        else (chr(encr) if encr <= 122 else chr(encr - 26))
