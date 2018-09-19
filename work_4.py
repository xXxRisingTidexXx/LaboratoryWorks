"""
Лабораторна робота №4
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN


def week_day():
    """
    #1
    """
    week = {1: 'понеділок', 2: 'вівторок', 3: 'середа', 4: 'четвер', 5: 'п\'ятниця', 6: 'субота', 7: 'неділя'}
    day = int(input('Введіть число місяця: ')) % 7
    print(week[day if day != 0 else 7])


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
    x1 = int(input()) % 2
    y1 = int(input()) % 2
    x2 = int(input()) % 2
    y2 = int(input()) % 2
    print('YES' if (0 if x1 == y1 else 1) == (0 if x2 == y2 else 1) else 'NO')


def are_on_the_same_line():
    """
    #4
    """
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print('YES' if x1 == x2 or y1 == y2 else 'NO')


def are_on_the_same_diagonal():
    """
    #5
    """
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print('YES' if abs(x2 - x1) == abs(y2 - y1) else 'NO')


def are_on_the_horse_path():
    """
    #6
    """
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    available_cells = {(x1 + 1, y1 + 2), (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2),
                       (x1 - 1, y1 - 2), (x1 - 2, y1 - 1), (x1 - 2, y1 + 1), (x1 - 1, y1 + 2)}
    print('YES' if (x2, y2) in available_cells else 'NO')


def are_at_the_current_area():
    """
    #7
    """
    tolerance = '.001'
    x = Decimal(input()).quantize(Decimal(tolerance), rounding=ROUND_HALF_EVEN)
    y = Decimal(input()).quantize(Decimal(tolerance), rounding=ROUND_HALF_EVEN)
    vertical = Decimal(2).quantize(Decimal(tolerance), rounding=ROUND_HALF_EVEN)
    r = Decimal(4).quantize(Decimal(tolerance), rounding=ROUND_HALF_EVEN)
    sqr_sum = Decimal(x * x + y * y).quantize(Decimal(tolerance), rounding=ROUND_HALF_EVEN)
    print('YES' if x.compare(y) > 0 and vertical.compare(x) > 0 and sqr_sum.compare(r) > 0 else 'NO')
