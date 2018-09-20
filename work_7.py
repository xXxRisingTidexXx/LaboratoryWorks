"""
Лабораторна робота №7
ІПЗ - 12, Петраківський Данило
"""
from random import randint, uniform
from math import sqrt
from work_4 import to_decimal
from numpy import roll


def calc_number_digits():
    """
    #1
    """
    for i in range(5):
        print(digest(randint(10000, 1000000)))


def digest(n):
    s = str(n)
    sum_ = 0
    for d in s:
        sum_ += int(d)
    return '{} {} {}'.format(n, len(s), sum_)


def invert_number():
    """
    #2
    """
    for i in range(5):
        print(invert(randint(10000, 1000000)))


def invert(n):
    s = str(n)[::-1]
    for i in range(len(s)):
        if s[i] != '0':
            return '{} {}'.format(n, s[i:])
    return '0 0'


def draw_power_table():
    """
    #3
    """
    a = []
    b = []
    c = []
    d = []
    aml = 0
    bml = 0
    cml = 0
    dml = 0
    for i in range(5):
        powers = calc_powers(randint(-128, 127))
        a.append(powers[0])
        aml = max(aml, len(powers[0]))
        b.append(powers[1])
        bml = max(bml, len(powers[1]))
        c.append(powers[2])
        cml = max(cml, len(powers[2]))
        d.append(powers[3])
        dml = max(dml, len(powers[3]))
    for i in range(5):
        print(expand(a[i], aml), expand(b[i], bml), expand(c[i], cml), expand(d[i], dml), sep='|')


def calc_powers(n):
    a = '.1f'
    return str(n), format(n ** 2, a), format(n ** 3, a), format(n ** 4, a)


def expand(cell, ml):
    return '{}{}'.format(' ' * (ml - len(cell)), cell)


def draw_average_value_table():
    """
    #4
    """
    x = uniform(0, 100)
    y = []
    aa = []
    ag = []
    yml = 0
    aaml = 0
    agml = 0
    for i in range(3):
        ry = (uniform(0, 100))
        y.append(format(ry))
        yml = max(yml, len(y[i]))
        aa.append(format((x + ry) / 2))
        aaml = max(aaml, len(aa[i]))
        ag.append(format(sqrt(x * ry)))
        agml = max(agml, len(ag[i]))
    for i in range(3):
        print('{} {}'.format(x, expand(y[i], yml)), expand(aa[i], aaml), expand(ag[i], agml), sep='|')


def draw_rectangle_table():
    """
    #5
    """
    table = {'x1': [], 'y1': [], 'x2': [], 'y2': [], 'p': [], 's': []}
    x1ml = 0
    y1ml = 0
    x2ml = 0
    y2ml = 0
    pml = 0
    sml = 0
    for i in range(3):
        x1 = to_decimal(input())
        y1 = to_decimal(input())
        x2 = to_decimal(input())
        y2 = to_decimal(input())
        ps = calc_perimeter_and_square(x1, y1, x2, y2)
        table['x1'].append(str(x1))
        table['y1'].append(str(y1))
        table['x2'].append(str(x2))
        table['y2'].append(str(y2))
        table['p'].append(ps[0])
        table['s'].append(ps[1])
        x1ml = max(x1ml, len(table['x1'][i]))
        y1ml = max(y1ml, len(table['y1'][i]))
        x2ml = max(x2ml, len(table['x2'][i]))
        y2ml = max(y2ml, len(table['y2'][i]))
        pml = max(pml, len(table['p'][i]))
        sml = max(sml, len(table['s'][i]))
    print('|{}x1{}'.format(' ' * ((x1ml - 1) // 2), ' ' * (x1ml - (x1ml - 1) // 2 - 2)),
          '{}y1{}'.format(' ' * ((y1ml - 1) // 2), ' ' * (y1ml - (y1ml - 1) // 2 - 2)),
          '{}x2{}'.format(' ' * ((x2ml - 1) // 2), ' ' * (x2ml - (x2ml - 1) // 2 - 2)),
          '{}y2{}'.format(' ' * ((y2ml - 1) // 2), ' ' * (y2ml - (y2ml - 1) // 2 - 2)),
          '{}p{}'.format(' ' * ((pml - 1) // 2), ' ' * (pml - (pml - 1) // 2 - 1)),
          '{}s{}|'.format(' ' * ((sml - 1) // 2), ' ' * (sml - (sml - 1) // 2 - 1)), sep='|')
    for i in range(3):
        print('|{}'.format(expand(table['x1'][i], x1ml)), expand(table['y1'][i], y1ml),
              expand(table['x2'][i], x2ml), expand(table['y2'][i], y2ml),
              expand(table['p'][i], pml), '{}|'.format(expand(table['s'][i], sml)), sep='|')


def calc_perimeter_and_square(x1, y1, x2, y2):
    if x1.compare(x2) == 0 or y1.compare(y2) == 0:
        return 'undefined', 'undefined'
    else:
        x = abs(x2 - x1)
        y = abs(y2 - y1)
        return str(2 * x + 2 * y), str(x * y)


def perform_right_shift():
    """
    #6
    """
    list1 = [uniform(-256, 255), uniform(-256, 255), uniform(-256, 255)]
    list2 = [uniform(-256, 255), uniform(-256, 255), uniform(-256, 255)]
    print(list1)
    print(roll(list1, 1))
    print(list2)
    print(roll(list2, 1))


def perform_left_shift():
    """
    #7
    """
    list1 = [uniform(-256, 255), uniform(-256, 255), uniform(-256, 255)]
    list2 = [uniform(-256, 255), uniform(-256, 255), uniform(-256, 255)]
    print(list1)
    print(roll(list1, -1))
    print(list2)
    print(roll(list2, -1))
