"""
Лабораторна робота №13
ІПЗ - 12, Петраківський Данило
"""
from work_4 import decimalize


def combine_lists():
    """
    #1
    """
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    b = []
    for i in range(n):
        b.append(int(input()))
    c = []
    for i in range(n):
        c.append(max(a[i], b[i]))
    print(c)


def filter_elements():
    """
    #2
    """
    a = input().split()
    b = a[::3]
    print('b.length: {}  b: {}'.format(len(b), b))


def shuffle_elements():
    """
    #3
    """
    a = input().split()
    print(a[::2] + a[1::2])


def supply_list():
    """
    #4
    """
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    b = [a[0]]
    for i in range(1, n):
        b.append((i * b[i - 1] + a[i]) / (i + 1))
    print(b)


def allocate_elements():
    """
    #5
    """
    n = int(input())
    b = []
    c = []
    for i in range(n):
        element = decimalize(input())
        if element.compare(0) >= 0:
            b.append(element)
        else:
            c.append(element)
    print('b.length: {}  b: {}'.format(len(b), b))
    print('c.length: {}  c: {}'.format(len(c), c))


def merge_two_lists():
    """
    #6
    """
    a = [-5, 0, 34, 37, 87]
    b = [-34, -7, -2, 0, 21]
    print(merge_asc(a, b))


def merge_asc(a, b):
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
    na = int(input())
    a = []
    for i in range(na):
        a.append(int(input()))
    nb = int(input())
    b = []
    for i in range(nb):
        b.append(int(input()))
    nc = int(input())
    c = []
    for i in range(nc):
        c.append(int(input()))
    print(merge_desc(merge_desc(a, b), c))


def merge_desc(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(b[j])
            j += 1
        elif b[j] < a[i]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[i])
            i += 1
            j += 1
    if i != len(a):
        c += a[i:]
    if j != len(b):
        c += b[j:]
    return c
