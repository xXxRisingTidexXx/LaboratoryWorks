"""
Лабораторна робота №18
ІПЗ - 12, Петраківський Данило
"""


def swap_rows():
    """
    #1
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    k1 = int(input('Введіть k1: ')) - 1
    k2 = int(input('Введіть k2: ')) - 1
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    buffer = matrix[k1]
    matrix[k1] = matrix[k2]
    matrix[k2] = buffer
    print(matrix)


def swap_columns():
    """
    #2
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    k1 = int(input('Введіть k1: ')) - 1
    k2 = int(input('Введіть k2: ')) - 1
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    for i in range(m):
        buffer = matrix[i][k1]
        matrix[i][k1] = matrix[i][k2]
        matrix[i][k2] = buffer
    print(matrix)


def swap_upper_and_lower_halves():
    """
    #3
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    print(matrix[m // 2:] + matrix[:m // 2])


def swap_left_and_right_halves():
    """
    #4
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    mid = n // 2
    for i in range(m):
        for j in range(mid + n % 2):
            buffer = matrix[i][j]
            matrix[i][j] = matrix[i][j + mid]
            matrix[i][j + mid] = buffer
    print(matrix)


def pop_row():
    """
    #5
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: ')) - 1
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    matrix.pop(k)
    print(matrix)


def pop_column():
    """
    #6
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: ')) - 1
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    for row in matrix:
        row.pop(k)
    print(matrix)


def insert_null_row():
    """
    #7
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: ')) - 1
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    matrix.insert(k, [0.0] * n)
    print(matrix)
