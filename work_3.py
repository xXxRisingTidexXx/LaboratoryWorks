"""
Лабораторна робота №3
ІПЗ - 12, Петраківський Данило
"""
from math import modf, sqrt, log, e, sin, fabs, ceil


def calc_fraction():
    """
    #1
    """
    x = float(input('Введіть х: '))
    print(format(modf(x)[0], '.4f'))


def calc_first_digit():
    """
    #2
    """
    x = str(float(input('Введіть х: ')))
    print(x[x.index('.') + 1])


def calc_formula():
    """
    #3
    """
    x = float(input('Введіть х: '))
    print(format(sqrt(log(4 / 3 + x, e) + 9 / 7) - e ** (-sin(1.3 * x - 0.7)), '.4f'))


def calc_man_perfect_weight():
    """
    #4
    """
    height = float(input('Введіть ваш зріст: '))
    weight = float(input('Введіть вашу масу: '))
    pw = height * 0.712 - 58
    print('Ваша ідеальна вага: {}\nКоригування: {}'.format(format(pw, '.3f'),
                                                           format(fabs(pw - weight), '.3f')))


def record_sound():
    """
    #5
    """
    v = float(input('Введіть v: '))
    d = float(input('Введіть d: '))
    t = float(input('Введіть t: '))
    print('{} Кбайт'.format(ceil(v * d * t / 8192)))


def determinate_time_1():
    """
    #6
    """
    h = float(input('Введіть h: '))
    m = float(input('Введіть m: '))
    s = float(input('Введіть s: '))
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
    print('{}:{}:{}'.format(extend(h), extend(m), extend(int(a // (0.5 / 60)))))


def extend(n):
    return str(n) if n >= 10 else '0{}'.format(n)
