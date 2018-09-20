"""
Лабораторна робота №5
ІПЗ - 12, Петраківський Данило
"""


def print_row():
    """
    #1
    """
    a = int(input('Введіть А: '))
    b = int(input('Введіть B: '))
    if a < b:
        printr(a, b + 1, 1)
    else:
        printr(a, b - 1, -1)


def printr(a, b, step):
    for i in range(a, b, step):
        print(i, end=' ')


def print_odd_numbers():
    """
    #2
    """
    ab = input('Введіть a, b: ').split()
    for i in range(int(ab[0]), int(ab[1]) + 1, 1):
        if i % 2 == 1:
            print(i, end=' ')


def factorial():
    """
    #3
    """
    n = int(input('Введіть n: '))
    f = 1
    for i in range(2, n + 1, 1):
        f *= i
    print(f)


def build_ladder():
    """
    #4
    """
    n = int(input('Введіть n: '))
    s = ''
    for i in range(1, n + 1, 1):
        s += str(i)
        print(s)


def build_multiplication_table():
    """
    #5
    """
    numbers = input('Введіть a, b: ').split()
    a = int(numbers[0])
    b = int(numbers[1])
    for i in range(a, b + 1, 1):
        s = ''
        for j in range(1, b + 1, 1):
            mul = i * j
            s += '{} x {} = {}{}'.format(i, j, mul, '' if j == b else (' | ' if mul >= 10 else '  | '))
        print(s)


def calc_zero_count():
    """
    #6
    """
    n = input('Введіть n: ')
    zero_count = 0
    for d in n:
        if d == '0':
            zero_count += 1
    print(zero_count)


def calc_sum_1():
    """
    #7
    """
    n = int(input('Введіть n: '))
    k = float(input('Введіть k: '))
    sum_ = 0.0
    for i in range(1, n + 1, 1):
        sum_ += i ** k
    print(sum_)


def calc_sum_2():
    """
    #8
    """
    n = int(input('Введіть n: '))
    sum_ = 0.0
    for i in range(1, n + 1, 1):
        sum_ += i ** i
    print(sum_)
