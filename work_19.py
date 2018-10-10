"""
Лабораторна робота №19
ІПЗ - 12, Петраківський Данило
"""


def calc_main_diagonal_sum():
    """
    #1
    """
    m = int(input('Введіть m: '))
    a = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)]
    print(sum([a[i][i] for i in range(m)]))


def calc_antidiagonal_average_value():
    """
    #2
    """
    m = int(input('Введіть m: '))
    a = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)]
    print(sum([a[i][m - 1 - i] for i in range(m)]) / m)


def transform_elements_1():
    """
    #3
    """
    m = int(input('Введіть m: '))
    a = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(i):
            a[i][j] = 0
    print(a)


def transform_elements_2():
    """
    #4
    """
    m = int(input('Введіть m: '))
    a = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)]
    for i in range(m - 1):
        for j in range(m - 2 - i, -1, -1):
            a[i][j] = 0
    print(a)


def transform_elements_3():
    """
    #5
    """
    m = int(input('Введіть m: '))
    a = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)]
    for i in range(m // 2):
        for j in range(i + 1, m - 1 - i):
            a[i][j] = 0
    print(a)


def mirror_elements():
    """
    #6
    """
    m = int(input('Введіть m: '))
    a = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(i):
            buffer = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = buffer
    print(a)
