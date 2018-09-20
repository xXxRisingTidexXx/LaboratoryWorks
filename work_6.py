"""
Лабораторна робота №6
ІПЗ - 12, Петраківський Данило
"""
from work_4 import to_decimal
from math import log10, sqrt, sin, pi


def calc_day():
    """
    #1
    """
    distance = to_decimal(10)
    percent = to_decimal(1.1)
    norm = to_decimal(25)
    day = 1
    while distance.compare(norm) < 0:
        distance *= percent
        day += 1
    print(day)


def calc_salary():
    """
    #2
    """
    x = int(input())
    a = int(input())
    print('{} грн.'.format(x if a <= 38 else x * (1 + 1.5 * (a - 38) / 38)))


def calc_percentage():
    """
    #3
    """
    x = to_decimal(input())
    p = to_decimal(float(input()) / 100.0)
    y = to_decimal(input())
    years = 0
    while y.compare(x) > 0:
        years += 1
        x = to_decimal(x + x * p)
    print('{} років'.format(years))


def calc_multiplication():
    """
    #4
    """
    a = int(input())
    b = int(input())
    m = 0
    for i in range(1, abs(b) + 1):
        m += abs(a)
    print(m if a >= 0 and b >= 0 or a < 0 and b < 0 else -m)


def calc_function():
    """
    #5
    """
    tolerance_ = '.001'
    a = to_decimal(input(), tolerance=tolerance_)
    b = to_decimal(input(), tolerance=tolerance_)
    d = to_decimal(input(), tolerance=tolerance_)
    while a.compare(b) <= 0:
        print(a, f(float(a)))
        a += d


def f(x):
    try:
        return format(log10(3) + x * sqrt(5 * sin(pi * x / 3)), '.3f')
    except ValueError:
        return 'undefined'


def calc_satisfactory_numbers():
    """
    #6
    """
    for i in range(10000, 100000):
        if i % 133 == 125 and i % 134 == 111:
            print(i)


def calc_armstrong_numbers():
    """
    #7
    """
    for i in range(100, 1000):
        if i == calc_digit_sum(i):
            print(i)


def calc_digit_sum(n):
    s = (n % 10) ** 3
    n //= 10
    s += (n % 10) ** 3
    return s + (n // 10) ** 3
