"""
Лабораторна робота №6
ІПЗ - 12, Петраківський Данило
"""
from work_4 import decimalize
from math import log10, sqrt, sin, pi
from decimal import ROUND_DOWN


def calc_day():
    """
    #1
    """
    distance = decimalize(10)
    percent = decimalize(1.1)
    norm = decimalize(25)
    day = 1
    while distance.compare(norm) < 0:
        distance *= percent
        day += 1
    print(day)


def calc_salary():
    """
    #2
    """
    numbers = input().split()
    x = int(numbers[0])
    a = int(numbers[1])
    print('{} грн.'.format(x if a <= 38 else x * (1 + 1.5 * (a - 38) / 38)))


def calc_percentage():
    """
    #3
    """
    numbers = input().split()
    x = decimalize(numbers[0])
    p = decimalize(float(numbers[1]) / 100.0)
    y = decimalize(numbers[2])
    years = 0
    while y.compare(x) > 0:
        years += 1
        x = decimalize(x + decimalize(x * p, rounding_=ROUND_DOWN))
    print('{} років'.format(years))


def calc_multiplication():
    """
    #4
    """
    numbers = input().split()
    x = int(numbers[0])
    a = int(numbers[1])
    m = 0
    for i in range(1, abs(a) + 1):
        m += abs(x)
    print(m if x >= 0 and a >= 0 or x < 0 and a < 0 else -m)


def calc_function():
    """
    #5
    """
    tolerance_ = '.001'
    a = decimalize(input(), tolerance=tolerance_)
    b = decimalize(input(), tolerance=tolerance_)
    d = decimalize(input(), tolerance=tolerance_)
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
        if i == dsum(i):
            print(i)


def dsum(n):
    s = (n % 10) ** 3
    n //= 10
    s += (n % 10) ** 3
    return s + (n // 10) ** 3
