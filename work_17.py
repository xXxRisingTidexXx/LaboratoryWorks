"""
Лабораторна робота №17
ІПЗ - 12, Петраківський Данило
"""


def build_list_based_matrix():
    """
    #1
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][0]: '.format(i)))] * n for i in range(m)]
    print(matrix)


# noinspection PyUnusedLocal
def build_arithmetic_progression_matrix():
    """
    #2
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    d = float(input('Введіть d: '))
    matrix = [[0.0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = float(input('matrix[{}][{}]: '.format(i, j))) if j == 0 else matrix[i][j - 1] + d
    print(matrix)


# noinspection PyUnusedLocal
def build_geometric_progression_matrix():
    """
    #3
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    q = float(input('Введіть q: '))
    matrix = [[0.0 for j in range(n)] for i in range(m)]
    for j in range(n):
        for i in range(m):
            matrix[i][j] = float(input('matrix[{}][{}]: '.format(i, j))) if i == 0 else matrix[i - 1][j] * q
    print(matrix)


def print_matrix_by_rows():
    """
    #4
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    for i in range(m):
        print(matrix[i][::(-1) ** i])


def print_matrix_by_columns():
    """
    #5
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            print(matrix[i if j % 2 == 0 else m - i - 1][j], end='\n' if j == n - 1 else '  ')


def calc_column_sum_and_multiplication():
    """
    #6
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    k = int(input('Введіть k: ')) - 1
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    total = 0
    mul = 1
    for i in range(m):
        total += matrix[i][k]
        mul *= matrix[i][k]
    print('сума: {}  добуток: {}'.format(total, mul))


def calc_row_sum():
    """
    #7
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    for row in matrix:
        print('сума: {}'.format(sum(row)))


def calc_arithmetic_average():
    """
    #8
    """
    m = int(input('Введіть m: '))
    n = int(input('Введіть n: '))
    matrix = [[float(input('matrix[{}][{}]: '.format(i, j))) for j in range(n)] for i in range(m)]
    for row in matrix[1::2]:
        print('середнє арифметичне: {}'.format(sum(row) / n))
