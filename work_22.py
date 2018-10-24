"""
Лабораторна робота №22
ІПЗ - 12, Петраківський Данило
"""
from struct import unpack, pack

ibuffer = 4
encoding = 'ascii'
cbuffer = 1


def collect_integer_files():
    """
    #1
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    main_filename = input('Введіть ім\'я головного файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'rb') as file_2, \
            open(filename_3, 'rb') as file_3, open(main_filename, 'wb') as main_file:
        bytes_1 = file_1.read()
        bytes_2 = file_2.read()
        bytes_3 = file_3.read()
        for i in range(0, len(bytes_1), ibuffer):
            s = slice(i, i + ibuffer)
            main_file.write(bytes_1[s])
            main_file.write(bytes_2[s])
            main_file.write(bytes_3[s])


def collect_and_sort_files():
    """
    #2
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    main_filename = input('Введіть ім\'я головного файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'rb') as file_2, open(main_filename, 'wb') as main_file:
        bytes_1 = file_1.read()
        bytes_2 = file_2.read()
        floats = [unpack('f', bytes_1[slice(i, i + ibuffer)])[0] for i in range(0, len(bytes_1), ibuffer)]
        floats.extend([unpack('f', bytes_2[slice(i, i + ibuffer)])[0] for i in range(0, len(bytes_2), ibuffer)])
        floats.sort()
        for f in floats:
            main_file.write(pack('f', f))


def archive_files():
    """
    #3
    """
    archive_name = input('Введіть ім\'я архіву: ')
    n = int(input('Введіть n: '))
    filenames = [input('Введіь ім\'я %d файлу: ' % (i + 1)) for i in range(n)]
    with open(archive_name, 'wb') as archives:
        archives.write(pack('i', n))
        lengths = []
        byte_lists = []
        for filename in filenames:
            with open(filename, 'rb') as file:
                byte_list = file.read()
                lengths.append(len(byte_list) // ibuffer)
                byte_lists.append(byte_list)
        for length in lengths:
            archives.write(pack('i', length))
        for byte_list in byte_lists:
            archives.write(byte_list)


def restore_file():
    """
    #4
    """
    destination_name = input('Введіть ім\'я цільового файлу: ')
    n = int(input('Введіть n: '))
    archive_name = input('Введіть ім\'я архіву: ')
    with open(archive_name, 'rb') as archives, open(destination_name, 'wb') as destination:
        total = unpack('i', archives.read(ibuffer))[0]
        if n <= total:
            offset = 0
            for i in range(n - 1):
                offset += unpack('i', archives.read(ibuffer))[0]
            length = unpack('i', archives.read(ibuffer))[0]
            archives.seek((1 + total + offset) * ibuffer)
            for i in range(length):
                destination.write(archives.read(ibuffer))


# noinspection PyUnusedLocal
def collect_float_files():
    """
    #5
    """
    destination_name = input('Введіть ім\'я цільового файлу: ')
    archive_name = input('Введіть ім\'я архіву: ')
    with open(archive_name, 'rb') as archives, open(destination_name, 'wb') as destination:
        total = unpack('i', archives.read(ibuffer))[0]
        lengths = [unpack('i', archives.read(ibuffer))[0] for i in range(total)]
        for length in lengths:
            destination.write(pack('f', sum([unpack('i', archives.read(ibuffer))[0] for i in range(length)]) / length))


def archive_integer_file():
    """
    #6
    """
    archive_name = input('Введіть ім\'я архіву: ')
    n = int(input('Введіть n: '))
    filenames = [input('Введіь ім\'я %d файлу: ' % (i + 1)) for i in range(n)]
    with open(archive_name, 'wb') as archives:
        for filename in filenames:
            with open(filename, 'rb') as file:
                byte_list = file.read()
                archives.write(pack('i', len(byte_list) // ibuffer))
                archives.write(byte_list)


def sort_character_file():
    """
    #7
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        byte_list = file.read()
        chars = [unpack('c', byte_list[slice(i, i + cbuffer)])[0].decode(encoding)
                 for i in range(0, len(byte_list), cbuffer)]
        chars.sort()
        file.seek(0)
        file.truncate()
        for char in chars:
            file.write(pack('c', char.encode(encoding)))


def sort_string_file():
    """
    #8
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        lines = [line for line in file.readlines()]
        lines.sort()
        file.seek(0)
        file.truncate()
        file.writelines(lines)
