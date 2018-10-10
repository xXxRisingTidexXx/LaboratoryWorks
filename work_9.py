"""
Лабораторна робота №9
ІПЗ - 12, Петраківський Данило
"""
from random import randint, uniform, sample


standard = '.3f'


def calc_factorial():
    """
    #1
    """
    for i in range(5):
        n = randint(1, 20)
        print('n: {}  n!: {}'.format(n, fac(n)))


def fac(n):
    return 1 if n == 1 else n * fac(n - 1)


def calc_double_factorial():
    """
    #2
    """
    for i in range(5):
        n = randint(1, 20)
        print('n: {}  n!!: {}'.format(n, dfac(n)))


def dfac(n):
    return 1 if n == 1 else 2 if n == 2 else n * dfac(n - 2)


def calc_combinations():
    """
    #3
    """
    n = randint(1, 20)
    for i in range(5):
        k = randint(1, n)
        c = comb(n, k)
        print('n: {}  k: {}  C(n, k): {}  recursive calls: {}'.format(n, k, c[0], c[1]))


def comb(n, k, i=0):
    if k == 0 or k == n:
        return 1, i + 1
    else:
        c1 = comb(n - 1, k, i + 1)
        c2 = comb(n - 1, k - 1, i + 1)
        return c1[0] + c2[0], c1[1] + c2[1]


def calc_digital_sum():
    """
    #4
    """
    for i in range(5):
        k = randint(-2048, 2047)
        print('k: {}  digital sum: {}'.format(k, dsum(abs(k), 0)))


def dsum(k, s):
    return s + k % 10 if k // 10 == 0 else s + k % 10 + dsum(k // 10, s)


def calc_sqrt_approximately():
    """
    #5
    """
    x = uniform(0.01, 4000)
    k = randint(2, 10)
    for i in range(5):
        n = randint(200, 400)
        print('x: {0}  k: {1}  n: {2}  {1}-root: {3}'.format(format(x, standard), k, n, format(y(x, n, k), standard)))


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
    a = randint(1, 500)
    b = randint(1, 500)
    c = randint(1, 500)
    d = randint(1, 500)
    print('gcd({}, {}): {}'.format(a, b, gcd(a, b)))
    print('gcd({}, {}): {}'.format(a, c, gcd(a, c)))
    print('gcd({}, {}): {}'.format(a, d, gcd(a, d)))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def calc_max():
    """
    #7
    """
    a = randint(1, 21)
    b = randint(1, 21)
    c = randint(1, 21)
    n = randint(1, 11)
    a1 = sample(range(-128, 128), n * a)
    a2 = sample(range(-128, 128), n * b)
    a3 = sample(range(-128, 128), n * c)
    print('n: {}  a: {}  max: {}'.format(n, a, amax(a1, a1[0])))
    print('n: {}  b: {}  max: {}'.format(n, b, amax(a2, a2[0])))
    print('n: {}  c: {}  max: {}'.format(n, c, amax(a3, a3[0])))


def amax(a, m):
    return m if len(a) == 0 else amax(a[1:], max(m, a[0]))


def calc_fibonacci():
    """
    #8
    """
    for i in range(5):
        n = randint(1, 21)
        f = fibo(n)
        print('n: {0}  f({0}): {1}  recursive calls: {2}'.format(n, f[0], f[1]))


def fibo(n, i=0):
    if n == 1 or n == 2:
        return 1, i + 1
    else:
        f1 = fibo(n - 1, i + 1)
        f2 = fibo(n - 2, i + 1)
        return f1[0] + f2[0], f1[1] + f2[1]
