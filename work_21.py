"""
Лабораторна робота №21
ІПЗ - 12, Петраківський Данило
"""
from struct import unpack, pack

buffer = 4


def write_squares():
    """
    #1
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        byte_list = file.read()
        file.seek(0)
        for i in range(0, len(byte_list), buffer):
            num = unpack('f', byte_list[slice(i, i + buffer)])[0]
            file.write(pack('f', num * num))


def rearrange_elements():
    """
    #2
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        byte_list = file.read()
        file.seek(0)
        i = 0
        j = len(byte_list) // buffer - 1
        while j - i > 1:
            file.write(byte_list[slice(i * buffer, (i + 1) * buffer)])
            file.write(byte_list[slice(j * buffer, (j + 1) * buffer)])
            i += 1
            j -= 1
        file.write(byte_list[slice(i * buffer, (i + 1) * buffer)])
        if j > i:
            file.write(byte_list[slice(j * buffer, (j + 1) * buffer)])


def copy():
    """
    #3
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'wb') as file_2:
        file_2.write(file_1.read())


def swap_contents():
    """
    #4
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'r+b') as file_1, open(filename_2, 'r+b') as file_2:
        bytes_1 = file_1.read()
        bytes_2 = file_2.read()
        file_1.seek(0)
        file_1.truncate()
        file_1.write(bytes_2)
        file_2.seek(0)
        file_2.truncate()
        file_2.write(bytes_1)


def collect_files():
    """
    #5
    """
    main_filename = input('Введіть ім\'я головного файлу: ')
    n = int(input('Введіть n: '))
    filenames = [input('Введіь ім\'я %d файлу: ' % i) for i in range(n)]
    with open(main_filename, 'wb') as main_file:
        for filename in filenames:
            with open(filename, 'rb') as file:
                main_file.write(file.read())


def append_data():
    """
    #6
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'r+b') as file_1, open(filename_2, 'r+b') as file_2:
        bytes_1 = file_1.read()
        bytes_2 = file_2.read()
        file_1.write(bytes_2)
        file_2.write(bytes_1)


def delete_data():
    """
    #7
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        byte_list = file.read()
        file.seek(0)
        file.truncate()
        length = len(byte_list)
        for i in range(length // 2, length, buffer):
            file.write(byte_list[slice(i, i + buffer)])


def double_contents():
    """
    #8
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        file.write(file.read())
