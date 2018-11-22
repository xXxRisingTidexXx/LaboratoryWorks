"""
Лабораторна робота №14
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN

STANDARD = '0.3f'


def swap_elements():
    """
    #1
    """
    n = int(input('Введіть n: '))
    a = [input('a[{}]: '.format(i + 1)) for i in range(n)]
    for i in range(1, len(a), 2):
        buffer = a[i - 1]
        a[i - 1] = a[i]
        a[i] = buffer
    print(' '.join(a))


def reverse_list():
    """
    #2
    """
    n = int(input('Введіть n: '))
    print(' '.join([input('a[{}]: '.format(i + 1)) for i in range(n)][::-1]))


def nullify_elements():
    """
    #3
    """
    n = int(input('Введіть n: '))
    a = [float(input('a[{}]: '.format(i + 1))) for i in range(n)]
    for i in range(a.index(min(a)) + 1, a.index(max(a))):
        a[i] = 0
    print(' '.join(map(lambda x: format(x, STANDARD), a)))


def remove_current_elements():
    """
    #4
    """
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    m = int(input('Введіть m: '))
    a = [input('a[{}]: '.format(i + 1)) for i in range(n)]
    print(' '.join(a[:k - 1] + a[m:]))


def remove_odd_indexed_elements():
    """
    #5
    """
    n = int(input('Введіть n: '))
    print(' '.join([input('a[{}]: '.format(i + 1)) for i in range(n)][::2]))


def add_element():
    """
    #6
    """
    n = int(input('Введіть n: '))
    k = int(input('Ввведіть k: '))
    a = [input('a[{}]: '.format(i + 1)) for i in range(n)]
    a.insert(k - 1, '0')
    print(' '.join(a))


def sort_list():
    """
    #7
    """
    n = int(input('Ввведіть n: '))
    print(' '.join(map(lambda x: format(x, STANDARD), sort(
        [decimalize(input('a[{}]: '.format(i + 1))) for i in range(n)]
    ))))


def decimalize(numb):
    return Decimal(numb).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)


def sort(a):
    return a if len(a) == 1 else merge(sort(a[:len(a) // 2]), sort(a[len(a) // 2:]))


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        elif b[j] > a[i]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[i])
            c.append(b[j])
            i += 1
            j += 1
    if i != len(a):
        c += a[i:]
    if j != len(b):
        c += b[j:]
    return c
