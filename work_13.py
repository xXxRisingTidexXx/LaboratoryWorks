"""
Лабораторна робота №13
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN


def combine_lists():
    """
    #1
    """
    n = int(input('Введіть n: '))
    a = [int(input('a[{}]: '.format(i))) for i in range(n)]
    b = [int(input('b[{}]: '.format(i))) for i in range(n)]
    c = [max(a[i], b[i]) for i in range(n)]
    print(c)


def filter_elements():
    """
    #2
    """
    a = input('Введіть масив: ').split()
    b = a[::3]
    print('b.length: {}  b: {}'.format(len(b), b))


def shuffle_elements():
    """
    #3
    """
    a = input('Введіть масив: ').split()
    print(a[::2] + a[1::2])


def supply_list():
    """
    #4
    """
    n = int(input('Введіть n: '))
    a = [int(input('a[{}]: '.format(i))) for i in range(n)]
    b = [a[0]]
    for i in range(1, n):
        b.append((i * b[i - 1] + a[i]) / (i + 1))
    print(b)


def allocate_elements():
    """
    #5
    """
    n = int(input('Введіть n: '))
    b = []
    c = []
    for i in range(n):
        element = decimalize(input('a[{}]: '.format(i)))
        if element.compare(0) >= 0:
            b.append(element)
        else:
            c.append(element)
    print('b.length: {}  b: {}'.format(len(b), b))
    print('c.length: {}  c: {}'.format(len(c), c))


def decimalize(numb):
    return Decimal(numb).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)


def merge_two_lists():
    """
    #6
    """
    a = [-5, 0, 34, 37, 87]
    b = [-34, -7, -2, 0, 21]
    print(merge(a, b))


# noinspection PyPep8Naming
def CASC(x, y):
    return x > y


# noinspection PyPep8Naming
def CDESC(x, y):
    return x < y


def merge(a, b, order=CASC):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if order(a[i], b[j]):
            c.append(b[j])
            j += 1
        elif order(b[j], a[i]):
            c.append(a[i])
            i += 1
        else:
            c.append(a[i])
            i += 1
            j += 1
    if i != len(a):
        c += a[i:]
    if j != len(b):
        c += b[j:]
    return c


def merge_three_lists():
    """
    #7
    """
    na = int(input('Введіть na: '))
    a = [int(input('a[{}]: '.format(i))) for i in range(na)]
    nb = int(input('Введіть nb: '))
    b = [int(input('b[{}]: '.format(i))) for i in range(nb)]
    nc = int(input('Введіть nc: '))
    c = [int(input('c[{}]: '.format(i))) for i in range(nc)]
    print(merge(merge(a, b, order=CDESC), c, order=CDESC))
