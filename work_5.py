"""
Лабораторна робота №5
ІПЗ - 12, Петраківський Данило
"""
from functools import reduce


def print_row():
    """
    #1
    """
    a = int(input('Введіть a: '))
    b = int(input('Введіть b: '))
    print(make_row(a, b + 1, 1) if a < b else make_row(a, b - 1, -1))


def make_row(a, b, step):
    return ' '.join([str(i) for i in range(a, b, step)])


def print_odd_numbers():
    """
    #2
    """
    ab = input('Введіть a, b: ').split()
    a = int(ab[0])
    print(' '.join([str(i) for i in range(a if a % 2 == 1 else a + 1, int(ab[1]) + 1, 2)]))


def calc_factorial():
    """
    #3
    """
    n = int(input('Введіть n: '))
    print(reduce(lambda fac, seq: fac * seq, [i for i in range(1, n + 1, 1)]))


def draw_ladder():
    """
    #4
    """
    n = int(input('Введіть n: '))
    print('\n'.join([''.join([str(j) for j in range(1, i + 1)]) for i in range(1, n + 1)]))


def draw_multiplication_table():
    """
    #5
    """
    numbers = input('Введіть a, b: ').split()
    b = int(numbers[1])
    print('\n'.join([' | '.join([make_cell(i, j) for j in range(1, b + 1)]) for i in range(int(numbers[0]), b + 1)]))


def make_cell(i, j):
    mul = i * j
    return '{} x {} = {}{}'.format(i, j, mul, ' ' if mul < 10 else '')


def calc_zero_count():
    """
    #6
    """
    n = input('Введіть n: ')
    print(len(list(filter(lambda d: d == '0', n))))


def calc_sum_1():
    """
    #7
    """
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    print(sum([i ** k for i in range(1, n + 1)]))


def calc_sum_2():
    """
    #8
    """
    n = int(input('Введіть n: '))
    print(sum([i ** i for i in range(1, n + 1)]))
