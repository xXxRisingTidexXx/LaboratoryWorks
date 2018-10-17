"""
Лабораторна робота №4
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN


def calc_week_day():
    """
    #1
    """
    week = ['неділя', 'понеділок', 'вівторок', 'середа', 'четвер', 'п\'ятниця', 'субота']
    day = int(input('Введіть число місяця: ')) % 7
    print(week[day])


def is_leap_year():
    """
    #2
    """
    year = int(input('Введіть рік: '))
    print('YES' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 'NO')


def are_on_the_same_color_cells():
    """
    #3
    """
    x1 = int(input('Введіть x1: ')) % 2
    y1 = int(input('Введіть y1: ')) % 2
    x2 = int(input('Введіть x2: ')) % 2
    y2 = int(input('Введіть y2: ')) % 2
    print('YES' if (0 if x1 == y1 else 1) == (0 if x2 == y2 else 1) else 'NO')


def are_on_the_same_line():
    """
    #4
    """
    x1 = int(input('Введіть x1: '))
    y1 = int(input('Введіть y1: '))
    x2 = int(input('Введіть x2: '))
    y2 = int(input('Введіть y2: '))
    print('YES' if x1 == x2 or y1 == y2 else 'NO')


def are_on_the_same_diagonal():
    """
    #5
    """
    x1 = int(input('Введіть x1: '))
    y1 = int(input('Введіть y1: '))
    x2 = int(input('Введіть x2: '))
    y2 = int(input('Введіть y2: '))
    print('YES' if abs(x2 - x1) == abs(y2 - y1) else 'NO')


def are_on_the_horse_path():
    """
    #6
    """
    x1 = int(input('Введіть x1: '))
    y1 = int(input('Введіть y1: '))
    x2 = int(input('Введіть x2: '))
    y2 = int(input('Введіть y2: '))
    available_cells = {(x1 + 1, y1 + 2), (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2),
                       (x1 - 1, y1 - 2), (x1 - 2, y1 - 1), (x1 - 2, y1 + 1), (x1 - 1, y1 + 2)}
    print('YES' if (x2, y2) in available_cells else 'NO')


def are_at_the_current_area():
    """
    #7
    """
    x = decimalize(input('Введіть x: '))
    y = decimalize(input('Введіть y: '))
    vertical = decimalize(2)
    r = decimalize(4)
    sqr_sum = decimalize(x * x + y * y)
    print('YES' if x.compare(y) > 0 and vertical.compare(x) > 0 and sqr_sum.compare(r) > 0 else 'NO')


def decimalize(numb):
    return Decimal(numb).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)
