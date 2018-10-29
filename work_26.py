"""
Лабораторна робота №26
ІПЗ - 12, Петраківський Данило
"""
from decimal import Decimal, ROUND_HALF_EVEN


def invert_list():
    """
    #1
    """
    n = int(input('Введіть n: '))
    a = [input('Введіть a[{}]: '.format(i)) for i in range(n)]
    print(' '.join(invert(a)))


def invert(a):
    n = len(a)
    for i in range(n // 2):
        buffer = a[i]
        a[i] = a[n - 1 - i]
        a[n - 1 - i] = buffer
    return a


def clean_list():
    """
    #2
    """
    na = int(input('Введіть na: '))
    a = [decimalize(input('Введіть a[{}]: '.format(i))) for i in range(na)]
    nb = int(input('Введіть nb: '))
    b = [decimalize(input('Введіть b[{}]: '.format(i))) for i in range(nb)]
    nc = int(input('Введіть nc: '))
    c = [decimalize(input('Введіть c[{}]: '.format(i))) for i in range(nc)]
    ca = clean(a)
    cb = clean(b)
    cc = clean(c)
    print('len(a): {}, a: {}'.format(ca[0], ca[1]))
    print('len(b): {}, b: {}'.format(cb[0], cb[1]))
    print('len(c): {}, c: {}'.format(cc[0], cc[1]))


def decimalize(num):
    return Decimal(num).quantize(Decimal('.001'), rounding=ROUND_HALF_EVEN)


def clean(a):
    i = 1
    while i < len(a):
        if a[i].compare(a[i - 1]) < 0:
            a.remove(a[i])
        else:
            i += 1
    return len(a), a


def sort_list():
    """
    #3
    """
    na = int(input('Введіть na: '))
    a = [decimalize(input('Введіть a[{}]: '.format(i))) for i in range(na)]
    nb = int(input('Введіть nb: '))
    b = [decimalize(input('Введіть b[{}]: '.format(i))) for i in range(nb)]
    nc = int(input('Введіть nc: '))
    c = [decimalize(input('Введіть c[{}]: '.format(i))) for i in range(nc)]
    print('a: {}'.format(sort(a)))
    print('b: {}'.format(sort(b)))
    print('c: {}'.format(sort(c)))


def sort(a):
    a.sort()
    return a


def create_index_list():
    """
    #4
    """
    na = int(input('Введіть na: '))
    a = [float(input('Введіть a[{}]: '.format(i))) for i in range(na)]
    nb = int(input('Введіть nb: '))
    b = [float(input('Введіть b[{}]: '.format(i))) for i in range(nb)]
    nc = int(input('Введіть nc: '))
    c = [float(input('Введіть c[{}]: '.format(i))) for i in range(nc)]
    print('ai: {}'.format(map_to_indices(a)))
    print('bi: {}'.format(map_to_indices(b)))
    print('ci: {}'.format(map_to_indices(c)))


def map_to_indices(a):
    pairs = [(a[i], i) for i in range(len(a))]
    pairs.sort(key=lambda pair: pair[0])
    return list(map(lambda pair: pair[1], pairs))


def reduce_list():
    """
    #5
    """
    n = int(input('Введіть n: '))
    a = [float(input('Введіть a[{}]: '.format(i))) for i in range(n)]
    bc = reduce(a)
    print('b: {}'.format(bc[0]))
    print('c: {}'.format(bc[1]))


def reduce(a):
    return a[1::2], a[::2]


def create_chess_matrix():
    """
    #6
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = create(m, n)
    for i in range(m):
        print(''.join(matrix[i]))


def create(m, n):
    return [[str((i + j) % 2) for j in range(n)] for i in range(m)]


def transpose_matrix():
    """
    #7
    """
    m = int(input('Введіть m: '))
    a = transpose([[float(input('Введіть a[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)])
    for i in range(m):
        for j in range(m):
            print(a[i][j], end=' ')
        print()


def transpose(a):
    m = len(a)
    for i in range(m):
        for j in range(i):
            buffer = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = buffer
    return a
