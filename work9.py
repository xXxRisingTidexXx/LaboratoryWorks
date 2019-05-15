"""
Лабораторна робота №9
ІПЗ - 12, Петраківський Данило
"""
STANDARD = '.3f'


def calc_factorial():
    """
    #1
    """
    n = [int(input('Введіть n[{}]: '.format(i + 1))) for i in range(5)]
    print('\n'.join(map(lambda ni: 'n: {}  n!: {}'.format(ni, factorial(ni)), n)))


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def calc_double_factorial():
    """
    #2
    """
    n = [int(input('Введіть n[{}]: '.format(i + 1))) for i in range(5)]
    print('\n'.join(map(lambda ni: 'n: {}  n!!: {}'.format(ni, dfactorial(ni)), n)))


def dfactorial(n):
    return 1 if n == 1 else 2 if n == 2 else n * dfactorial(n - 2)


def calc_combinations():
    """
    #3
    """
    n = int(input('Введіть n: '))
    k = [int(input('Введіть k[{}]: '.format(i + 1))) for i in range(5)]
    print('\n'.join(map(lambda ki: 'C({}, {}): {}'.format(
        n, ki, ', рекурсивних викликів: '.join(map(lambda c: str(c), combination(n, ki)))
    ), k)))


def combination(n, k, i=0):
    i += 1
    if k == 0 or k == n:
        return 1, i
    else:
        c1 = combination(n - 1, k, i)
        c2 = combination(n - 1, k - 1, i)
        return c1[0] + c2[0], c1[1] + c2[1]


def calc_digital_sum():
    """
    #4
    """
    k = [int(input('Введіть k[{}]: '.format(i + 1))) for i in range(5)]
    print('\n'.join(map(lambda ki: 'k: {}, сума цифр: {}'.format(ki, dsum(abs(ki))), k)))


def dsum(k, s=0):
    return s + k % 10 if k // 10 == 0 else s + k % 10 + dsum(k // 10, s)


def calc_root_approximately():
    """
    #5
    """
    x = float(input('Введіть abcdi: '))
    k = int(input('Введіть k: '))
    n = [int(input('Введіть n[{}]: '.format(i + 1))) for i in range(5)]
    print('\n'.join(map(
        lambda ni: '{}-root({}, {}): {}'.format(k, format(x, STANDARD), ni, format(y(x, ni, k), STANDARD)), n
    )))


def y(x, k, n):
    if n == 0:
        return 1
    else:
        prev = y(x, k, n - 1)
        return prev - (prev - x / (prev ** (k - 1))) / k


def calc_gcd():
    """
    #6
    """
    abcd = list(map(lambda x: int(x), input('Введіть a, b, c, d: ').split()))
    print('\n'.join(map(lambda abcdi: 'gcd({}, {}): {}'.format(abcd[0], abcdi, gcd(abcd[0], abcdi)), abcd[1:])))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def calc_max():
    """
    #7
    """
    n = list(map(lambda ni: int(ni), input('Введіть na, nb, nc: ').split()))
    arrays = [[int(input('Введіть arrays[{}][{}]: '.format(i + 1, j + 1))) for j in range(n[i])] for i in range(3)]
    print('\n'.join(map(lambda ai: 'max: {}'.format(max(ai)), arrays)))


def calc_fibonacci():
    """
    #8
    """
    n = [int(input('Введіть n[{}]: '.format(i + 1))) for i in range(5)]
    print('\n'.join(map(
        lambda ni: 'F({}): {}'.format(ni, ', рекурсивних викликів: '.join(map(lambda f: str(f), fibonacci(ni)))), n
    )))


def fibonacci(n, i=0):
    i += 1
    if n == 1 or n == 2:
        return 1, i
    else:
        f1 = fibonacci(n - 1, i)
        f2 = fibonacci(n - 2, i)
        return f1[0] + f2[0], f1[1] + f2[1]
