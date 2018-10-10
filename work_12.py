"""
Лабораторна робота №12
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN

standard = '.3f'


def build_progression():
    """
    #1
    """
    n = int(input('Введіть n: '))
    a = float(input('Введіть a: '))
    d = float('Введіть d: ')
    progression = [a + i * d for i in range(n)]
    print(progression)


def build_super_sum_list():
    """
    #2
    """
    n = int(input('Введіть n: '))
    a = int(input('Введіть a: '))
    b = int(input('Введіть b: '))
    seq = [a, b, a + b]
    for i in range(3, n):
        seq.append(seq[i - 1] * 2)
    print(seq)


def build_k_indexed_list():
    """
    #3
    """
    k = int(input('Введіть k: '))
    seq = input('Введіть масив: ').split()
    print(seq[::k])


def build_odd_and_even_indexed_lists():
    """
    #4
    """
    seq = input('Введіть масив: ').split()
    print(seq[::2])
    print(seq[1::2])


def calc_snapshot_sum():
    """
    #5
    """
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    m = int(input('Введіть m: '))
    seq = [float(input('seq[{}]: '.format(i))) for i in range(n)]
    print(sum(seq[k - 1:m]))


def calc_min_element():
    """
    #6
    """
    n = int(input('Введіть n: '))
    seq = [decimalize(input('seq[{}]: '.format(i))) for i in range(n)]
    print(min(seq[::2]))


def decimalize(numb):
    return Decimal(numb).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)


def calc_max_element():
    """
    #7
    """
    n = int(input('Введіть n: '))
    seq = [decimalize(input('seq[{}]: '.format(i))) for i in range(n)]
    print(max(seq[1::2]))


def calc_closest_element():
    """
    #8
    """
    n = int(input('Введіть n: '))
    r = float(input('Введіть r: '))
    seq = [float(input('seq[{}]: '.format(i))) for i in range(n)]
    closest = seq[0]
    for i in range(1, n):
        closest = closest if decimalize(abs(closest - r)).compare(decimalize(abs(seq[i] - r))) <= 0 else seq[i]
    print(format(closest, standard))
