"""
Лабораторна робота №20
ІПЗ - 12, Петраківський Данило
"""
from struct import pack, unpack

buffer = 4


def create_integer_file():
    """
    #1
    """
    filename = input('Введіть ім\'я файлу: ')
    n = int(input('Введіть n: '))
    with open(filename, 'wb') as file:
        for i in range(1, n + 1):
            file.write(pack('i', i * 2))


def create_arithmetic_progression_file():
    """
    #2
    """
    filename = input('Введіть ім\'я файлу: ')
    a = float(input('Введіть a: '))
    d = float(input('Введіть d: '))
    with open(filename, 'wb') as file:
        for i in range(10):
            file.write(pack('f', a + d * i))


def print_file_element():
    """
    #3
    """
    filename = input('Введіть ім\'я файлу: ')
    k = int(input('Введіть k: ')) - 1
    with open(filename, 'rb') as file:
        file.seek(k * buffer)
        print(unpack('I', file.read(buffer))[0])


def create_absent_file():
    """
    #4
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'wb') as file_2:
        byte_list = file_1.read()
        length = len(byte_list)
        file_2.write(byte_list[slice(0, buffer)])
        file_2.write(byte_list[slice(length - buffer, length)])


def create_equal_file():
    """
    #5
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'wb') as file_2:
        byte_list = file_1.read()
        for i in range(len(byte_list), 0, -buffer):
            file_2.write(byte_list[slice(i - buffer, i)])


def create_two_partial_files():
    """
    #6
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'wb') as file_2, open(filename_3, 'wb') as file_3:
        byte_list = file_1.read()
        for i in range(0, len(byte_list), buffer):
            if i % 2 == 1:
                file_2.write(byte_list[slice(i, i + buffer)])
            else:
                file_3.write(byte_list[slice(i, i + buffer)])


def parse_file_elements():
    """
    #7
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'rb') as file:
        s = 0.0
        m = 1.0
        byte_list = file.read()
        length = len(byte_list)
        for i in range(0, length, buffer):
            num = unpack('f', byte_list[slice(i, i + buffer)])[0]
            s += num
            m *= num
        print('average arithmetic: %f  average geometric: %f' %
              (s / length * buffer, m ** (1 / length * buffer)))

# create_integer_file()
# with open('res/ints', 'rb') as file:
#     byte_list = file.read()
#     for i in range(0, len(byte_list), buffer):
#         print(unpack('i', byte_list[slice(i, i + buffer)])[0])
#
