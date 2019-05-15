"""
Лабораторна робота №13
ІПЗ - 12, Петраківський Данило
"""
STANDARD = '.3f'


def combine_lists():
    """
    #1
    """
    n = int(input('Введіть n: '))
    a = [float(input('a[{}]: '.format(i + 1))) for i in range(n)]
    b = [float(input('b[{}]: '.format(i + 1))) for i in range(n)]
    print(' '.join(map(lambda x: str(x), [max(a[i], b[i]) for i in range(n)])))


def filter_elements():
    """
    #2
    """
    n = int(input('Введіть n: '))
    b = [input('a[{}]: '.format(i + 1)) for i in range(n)][::3]
    print('len(b): {}  b: {}'.format(len(b), ' '.join(b)))


def shuffle_elements():
    """
    #3
    """
    n = int(input('Введіть n: '))
    a = [input('a[{}]: '.format(i + 1)) for i in range(n)]
    print(' '.join(a[::2] + a[1::2]))


def supply_list():
    """
    #4
    """
    n = int(input('Введіть n: '))
    a = [float(input('a[{}]: '.format(i + 1))) for i in range(n)]
    b = [a[0]]
    for i in range(1, n):
        b.append((i * b[i - 1] + a[i]) / (i + 1))
    print(' '.join(map(lambda x: format(x, STANDARD), b)))


def allocate_elements():
    """
    #5
    """
    n = int(input('Введіть n: '))
    a = [float(input('a[{}]: '.format(i + 1))) for i in range(n)]
    b = list(filter(lambda x: x >= 0, a))
    c = list(filter(lambda x: x < 0, a))
    print('len(b): {}  b: {}'.format(len(b), ' '.join(map(lambda x: format(x, STANDARD), b))))
    print('len(c): {}  c: {}'.format(len(c), ' '.join(map(lambda x: format(x, STANDARD), c))))


def merge_two_lists():
    """
    #6
    """
    a = [int(input('Введіть a[{}]: '.format(i + 1))) for i in range(5)]
    b = [int(input('Введіть b[{}]: '.format(i + 1))) for i in range(5)]
    print(' '.join(map(lambda x: str(x), merge(a, b))))


# noinspection PyPep8Naming
def ASC(x, y):
    return x > y


# noinspection PyPep8Naming
def DESC(x, y):
    return x < y


def merge(a, b, order=ASC):
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
            c.append(b[j])
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
    nb = int(input('Введіть nb: '))
    nc = int(input('Введіть nc: '))
    a = [int(input('a[{}]: '.format(i + 1))) for i in range(na)]
    b = [int(input('b[{}]: '.format(i + 1))) for i in range(nb)]
    c = [int(input('c[{}]: '.format(i + 1))) for i in range(nc)]
    print(' '.join(map(lambda x: str(x), merge(merge(a, b, order=DESC), c, order=DESC))))
