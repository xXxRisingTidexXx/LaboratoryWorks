"""
Лабораторна робота №14
ІПЗ - 12, Петраківський Данило
"""
from work_13 import merge_asc
from work_4 import decimalize


def swap_elements():
    """
    #1
    """
    a = input().split()
    for i in range(1, len(a), 2):
        buffer = a[i - 1]
        a[i - 1] = a[i]
        a[i] = buffer
    print(a)


def reverse_list():
    """
    #2
    """
    a = input().split()
    print(a[::-1])


def nullify_elements():
    """
    #3
    """

    n = int(input())
    a = []
    for i in range(n):
        a.append(float(input()))
    for i in range(a.index(min(a)) + 1, a.index(max(a))):
        a[i] = 0
    print(a)


def remove_current_elements():
    """
    #4
    """
    a = input().split()
    k = int(input()) - 1
    m = int(input()) - 1
    print(a[:k] + a[m + 1:])


def remove_odd_indexed_elements():
    """
    #5
    """
    a = input().split()
    print(a[::2])


def add_element():
    """
    #6
    """
    a = input().split()
    k = int(input()) - 1
    a.insert(k, '0')
    print(a)


def sort_list():
    """
    #7
    """
    n = int(input())
    a = []
    for i in range(n):
        a.append(decimalize(input()))
    print(sort(a))


def sort(a):
    return a if len(a) == 1 else merge_asc(sort(a[:len(a) // 2]), sort(a[len(a) // 2:]))
