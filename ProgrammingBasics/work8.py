"""
Лабораторна робота №8
ІПЗ - 12, Петраківський Данило
"""
from functools import reduce
from math import pi, sqrt

STANDARD = '.3f'


def calc_ring_square():
    """
    #1
    """
    for i in range(3):
        r1, r2 = map(lambda r: float(r), input('Введіть r1, r2 {} пари кілець: '.format(i + 1)).split())
        print('r1: {}  r2: {}  площа кільця: {}'.format(
            format(r1, STANDARD), format(r2, STANDARD), format(square(r1, r2), STANDARD)
        ))


def square(r1, r2):
    return (r1 * r1 - r2 * r2) * pi


def calc_random_number_sum():
    """
    #2
    """
    a, b, c = map(lambda x: int(x), input('Введіть a, b, c: ').split())
    print('sum({}, {}): {}'.format(a, b, add(a, b)))
    print('sum({}, {}): {}'.format(b, c, add(b, c)))


def add(a, b):
    return sum([i for i in range(a, b + 1)])


def perform_operations():
    """
    #3
    """
    a = float(input('Ввведіть a: '))
    b = float(input('Ввведіть b: '))
    o = int(input('Ввведіть операцію: '))
    operations = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
    print(format(operations[o if 1 <= o <= 3 else 0](a, b), '.3f'))


def check_squares():
    """
    #4
    """
    print('\n'.join([checkn(int(input('Введіть n[{}]: '.format(i + 1)))) for i in range(10)]))


def checkn(n):
    root = int(sqrt(n))
    return '{} {}'.format(n, root * root == n)


def convert_degrees():
    """
    #5
    """
    print('\n'.join([radians(float(input('Введіть d[{}]: '.format(i + 1)))) for i in range(5)]))


def radians(d):
    return 'deg: {}  rad: {}'.format(format(d, STANDARD), format(pi * d / 180, STANDARD))


def calc_double_factorial():
    """
    #6
    """
    print('\n'.join([dfactorial(int(input('Введіть n[{}]: '.format(i + 1)))) for i in range(5)]))


def dfactorial(n):
    return 'n: {}  n!!: {}'.format(n, reduce(lambda x, y: x * y, [i for i in range(1 if n % 2 == 1 else 2, n + 1, 2)]))
