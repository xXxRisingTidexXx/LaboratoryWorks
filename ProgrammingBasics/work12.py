"""
Лабораторна робота №12
ІПЗ - 12, Петраківський Данило
"""
STANDARD = '.3f'


def build_progression():
    """
    #1
    """
    n = int(input('Введіть n: '))
    a = float(input('Введіть a: '))
    d = float(input('Введіть d: '))
    print(' '.join(map(lambda x: format(x, STANDARD), [a + i * d for i in range(n)])))


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
    print(' '.join(map(lambda x: str(x), seq)))


def build_k_indexed_list():
    """
    #3
    """
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    print(' '.join([input('a[{}]: '.format(i + 1)) for i in range(n)][::k]))


def build_odd_and_even_indexed_lists():
    """
    #4
    """
    n = int(input('Введіть n: '))
    a = [input('a[{}]: '.format(i + 1)) for i in range(n)]
    print(' '.join(a[::2]))
    print(' '.join(a[1::2]))


def calc_snapshot_sum():
    """
    #5
    """
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: '))
    m = int(input('Введіть m: '))
    print(sum([float(input('a[{}]: '.format(i + 1))) for i in range(n)][k - 1:m]))


def calc_min_element():
    """
    #6
    """
    n = int(input('Введіть n: '))
    print(min([float(input('a[{}]: '.format(i + 1))) for i in range(n)][::2]))


def calc_max_element():
    """
    #7
    """
    n = int(input('Введіть n: '))
    print(max([float(input('a[{}]: '.format(i + 1))) for i in range(n)][1::2]))


def calc_closest_element():
    """
    #8
    """
    n = int(input('Введіть n: '))
    r = float(input('Введіть r: '))
    print(min([float(input('a[{}]: '.format(i + 1))) for i in range(n)], key=lambda x: abs(x - r)))
