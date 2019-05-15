"""
Лабораторна робота №7
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN
from math import sqrt
from random import randint
from re import match
from numpy import roll


# noinspection PyUnusedLocal
def calc_number_digits():
    """
    #1
    """
    print('\n'.join([digest(randint(10000, 1000000)) for i in range(5)]))


def digest(n):
    s = str(n)
    return '{} {} {}'.format(n, len(s), sum(map(lambda ch: int(ch), s)))


# noinspection PyUnusedLocal
def invert_number():
    """
    #2
    """
    print('\n'.join([invert(randint(10000, 1000000)) for i in range(5)]))


def invert(n):
    return '{} {}'.format(n, match(r'^0*(\d+)$', str(n)[::-1]).group(1))


def draw_power_table():
    """
    #3
    """
    print('\n'.join(map(lambda row: '|'.join(row), format_table(
        [calc_powers(int(input('Введіть {} число: '.format(i + 1)))) for i in range(5)]
    ))))


def calc_powers(n):
    t = '.1f'
    return [str(n), format(n * n, t), format(n * n * n, t), format(n ** 4, t)]


def format_table(table):
    m = len(table)
    n = len(table[0])
    cell_widths = [max(map(lambda s: len(s), [table[i][j] for i in range(m)])) for j in range(n)]
    return [['{:>{}}'.format(table[i][j], cell_widths[j]) for j in range(n)] for i in range(m)]


def draw_average_value_table():
    """
    #4
    """
    abcd = list(map(lambda s: float(s), input('Введіть a, b, c, d: ').split()))
    print('\n'.join(map(lambda row: '|'.join(row), format_table(
        [[str(abcd[0]), str(abcd[1]), format((abcd[0] + abcd[1]) / 2, '.2f'), format(sqrt(abcd[0] * abcd[1]), '.5f')],
         [str(abcd[0]), str(abcd[2]), format((abcd[0] + abcd[2]) / 2, '.2f'), format(sqrt(abcd[0] * abcd[2]), '.5f')],
         [str(abcd[0]), str(abcd[3]), format((abcd[0] + abcd[3]) / 2, '.2f'), format(sqrt(abcd[0] * abcd[3]), '.5f')]]
    ))))


def draw_rectangle_table():
    """
    #5
    """
    print('\n'.join(map(lambda row: '|{}|'.format('|'.join(row)), add_header(format_table(
        [calc_rectangle(input('Введіть координати {}-го прямокутника: '.format(i + 1)).split()) for i in range(3)]
    )))))


def calc_rectangle(coordinates):
    dc = tuple(map(lambda s: decimalize(s), coordinates))
    if dc[0].compare(dc[2]) == 0 or dc[1].compare(dc[3]) == 0:
        ps = ['undefined', 'undefined']
    else:
        x = abs(dc[2] - dc[0])
        y = abs(dc[3] - dc[1])
        t = '.2f'
        ps = [format(2 * x + 2 * y, t), format(x * y, t)]
    return list(map(lambda d: format(d, '.1f'), dc)) + ps


def decimalize(numb):
    return Decimal(numb).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)


def add_header(table):
    captions = ['X1', 'Y1', 'X2', 'Y2', 'P', 'S']
    table.insert(0, ['{:^{}}'.format(captions[j], len(table[0][j])) for j in range(6)])
    return table


def right_circular_shift():
    """
    #6
    """
    for i in range(2):
        print(' '.join(roll(input('Введіть a, b, c: ').split(), 1)))


def left_circular_shift():
    """
    #7
    """
    for i in range(2):
        print(' '.join(roll(input('Введіть a, b, c: ').split(), -1)))
