"""
Лабораторна робота №3
ІПЗ - 12, Петраківський Данило
"""
import math
from work_2 import expand


def calculate_fractional_part():
    """
    #1
    """
    x = float(input('Введіть X: '))
    print(format(math.modf(x)[0], '.4f'))


def calculate_first_digit():
    """
    #2
    """
    x = input('Введіть X: ')
    print(x[x.index('.') + 1])


def calculate_formula():
    """
    #3
    """
    x = float(input('Введіть X: '))
    print(format(math.sqrt(math.log(4 / 3 + x, math.e) + 9 / 7) - math.e ** (-math.sin(1.3 * x - 0.7)), '.4f'))


def calculate_man_perfect_weight():
    """
    #4
    """
    height = float(input())
    weight = float(input())
    pw = height * 0.712 - 58
    print('Ваша ідеальна вага: {}\nКоригування: {}'.format(format(pw, '.3f'),
                                                           format(math.fabs(pw - weight), '.3f')))


def record_sound():
    """
    #5
    """
    v = float(input())
    d = float(input())
    t = float(input())
    print('{} Кбайт'.format(math.ceil(v * d * t / 8 / 1024)))


def determinate_time_1():
    """
    #6
    """
    h = float(input())
    m = float(input())
    s = float(input())
    print('{} град.'.format(format(30 * (h + m / 60 + s / 3600), '.2f')))


def determinate_time_2():
    """
    #7
    """
    a = float(input('Введіть a (град.): '))
    h = int(a // 30)
    a %= 30
    m = int(a // 0.5)
    a %= 0.5
    print('{}:{}:{}'.format(expand(h), expand(m), expand(int(a // (0.5 / 60)))))
