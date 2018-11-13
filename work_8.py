"""
Лабораторна робота №8
ІПЗ - 12, Петраківський Данило
"""
from functools import reduce
from random import randint, uniform
from math import pi


standard = '.3f'


def calc_ring_square():
    """
    #1
    """
    for i in range(3):
        r1 = uniform(200, 400)
        r2 = uniform(1, r1)
        print('r1: {}  r2: {}  ring square: {}'.format(format(r1, standard),
                                                       format(r2, standard),
                                                       format(compute_square(r1, r2), standard)))


def compute_square(r1, r2):
    return (r1 * r1 - r2 * r2) * pi


def calc_random_number_sum():
    """
    #2
    """
    a = randint(-128, 127)
    b = randint(-128, 127)
    c = randint(-128, 127)
    print('sum[{}, {}]: {}'.format(a, b, compute_sum(a, b)))
    print('sum[{}, {}]: {}'.format(b, c, compute_sum(b, c)))


def compute_sum(a, b):
    if a > b:
        return 0
    else:
        s = 0
        for i in range(a, b + 1):
            s += i
        return s


def perform_operations():
    """
    #3
    """
    a = float(input('Ввведіть a: '))
    b = float(input('Ввведіть b: '))
    o = int(input('Ввведіть operation: '))
    if o == 1:
        print(a - b)
    elif o == 2:
        print(a * b)
    elif o == 3:
        print(a / b)
    else:
        print(a + b)


def is_square():
    """
    #4
    """
    for i in range(10):
        n = randint(1, 10001)
        print(n, checkn(n))


def checkn(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False


def convert_degrees():
    """
    #5
    """
    for i in range(5):
        d = uniform(0, 1080)
        print('deg: {}  rad: {}'.format(format(d, standard), format(compute_radians(d), standard)))


def compute_radians(d):
    return pi * d / 180


def calc_double_factorial():
    """
    #6
    """
    for i in range(5):
        n = randint(1, 20)
        print('n: {}  n!!: {}'.format(n, computef(n)))


def computef(n):
    return reduce(lambda x, y: x * y, [i for i in range(1 if n % 2 == 1 else 2, n + 1, 2)])
