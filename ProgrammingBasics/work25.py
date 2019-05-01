"""
Лабораторна робота №25
ІПЗ - 12, Петраківський Данило
"""
from math import sin, cos
from re import compile


def build_two_column_table():
    """
    #1
    """
    width = 5
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    with open(filename_1, 'r') as file_1, open(filename_2, 'r') as file_2, open(filename_3, 'w') as file_3:
        lines_1 = file_1.read().split('\n')
        lines_2 = file_2.read().split('\n')
        file_3.write('\n'.join(
            ['|%s%s|' % (expand(lines_1[i], width), expand(lines_2[i], width)) for i in range(len(lines_1))]
        ))


def expand(placeholder, width, align='r'):
    complement = ' ' * (width - len(placeholder))
    return complement + placeholder if align == 'r' else placeholder + complement if align == 'l' else placeholder


def build_three_column_table():
    """
    #2
    """
    width = 10
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    filename_4 = input('Введіть ім\'я 4 файлу: ')
    with open(filename_1, 'r') as file_1, open(filename_2, 'r') as file_2, \
            open(filename_3, 'r') as file_3, open(filename_4, 'w') as file_4:
        lines_1 = file_1.read().split('\n')
        lines_2 = file_2.read().split('\n')
        lines_3 = file_3.read().split('\n')
        file_4.write('\n'.join(
            ['|%s%s%s|' % (expand(lines_1[i], width, 'l'), expand(lines_2[i], width, 'l'),
                           expand(lines_3[i], width, 'l')) for i in range(len(lines_1))]
        ))


def build_trigonometric_table():
    """
    #3
    """
    xwidth = 8
    fwidth = 12
    a = float(input('Введіть a: '))
    b = float(input('Введіть b: '))
    n = int(input('Введіть n: '))
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'w') as file:
        d = (b - a) / n
        lines = []
        for i in range(n + 1):
            x = a + i * d
            lines.append('|%s%s%s|' % (expand(format(x, '.4f'), xwidth),
                                       expand(format(sin(x), '.8f'), fwidth),
                                       expand(format(cos(x), '.8f'), fwidth)))
        file.write('\n'.join(lines))


def create_integer_file():
    """
    #4
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'r') as file_1, open(filename_2, 'w') as file_2:
        lines = []
        for line in file_1.readlines():
            for num in line.split():
                if '.' not in num:
                    lines.append(num)
        file_2.write('\n'.join(lines))


def parse_combined_file():
    """
    #5
    """
    twidth = 30
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    with open(filename_1, 'r') as file_1, open(filename_2, 'w') as file_2, open(filename_3, 'w') as file_3:
        lines_2 = []
        lines_3 = []
        for line in file_1.readlines():
            lines_2.append(line[:twidth])
            lines_3.append(line[twidth:])
        file_2.write('\n'.join(lines_2))
        file_3.write(''.join(lines_3))


def parse_float_file():
    """
    #6
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    filename_4 = input('Введіть ім\'я 4 файлу: ')
    with open(filename_1, 'r') as file_1, open(filename_2, 'w') as file_2, \
            open(filename_3, 'w') as file_3, open(filename_4, 'w') as file_4:
        pattern = compile(r'^ *([\d.-]+) *([\d.-]+) *([\d.-]+) *\n?$')
        lines_2 = []
        lines_3 = []
        lines_4 = []
        for line in file_1.readlines():
            groups = pattern.match(line)
            lines_2.append(groups[1])
            lines_3.append(groups[2])
            lines_4.append(groups[3])
        file_2.write('\n'.join(lines_2))
        file_3.write('\n'.join(lines_3))
        file_4.write('\n'.join(lines_4))


def create_sum_file():
    """
    #7
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    with open(filename_1, 'r') as file_1, open(filename_2, 'w') as file_2:
        pattern = compile(r'^\S *([\d-]+) *\S *([\d-]+) *\S *([\d-]+) *\S\n?$')
        lines_2 = []
        for line in file_1.readlines():
            groups = pattern.match(line)
            lines_2.append(str(int(groups[1]) + int(groups[2]) + int(groups[3])))
        file_2.write('\n'.join(lines_2))
