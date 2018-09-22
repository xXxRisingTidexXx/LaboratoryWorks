"""
Лабораторна робота №12
ІПЗ - 12, Петраківський Данило
"""
from work_4 import decimalize
from work_8 import standard


def build_progression():
    """
    #1
    """
    n = int(input())
    a = float(input())
    d = float(input())
    progression = [a] * n
    for i in range(n):
        progression[i] += i * d
    print(progression)


def build_super_sum_list():
    """
    #2
    """
    n = int(input())
    a = int(input())
    b = int(input())
    seq = [a, b, a + b]
    for i in range(3, n):
        seq.append(seq[i - 1] * 2)
    print(seq)


def build_k_indexed_list():
    """
    #3
    """
    k = int(input())
    seq = input().split()
    print(seq[::k])


def build_odd_and_even_indexed_lists():
    """
    #4
    """
    seq = input().split()
    print(seq[::2])
    print(seq[1::2])


def calc_snapshot_sum():
    """
    #5
    """
    n = int(input())
    k = int(input())
    m = int(input())
    seq = []
    for i in range(n):
        seq.append(float(input()))
    print(sum(seq[k - 1:m]))


def calc_min_element():
    """
    #6
    """
    n = int(input())
    seq = []
    for i in range(n):
        seq.append(decimalize(input()))
    print(min(seq[::2]))


def calc_max_element():
    """
    #7
    """
    n = int(input())
    seq = []
    for i in range(n):
        seq.append(decimalize(input()))
    print(max(seq[1::2]))


def calc_closest_element():
    """
    #8
    """
    n = int(input())
    r = float(input())
    seq = []
    for i in range(n):
        seq.append(float(input()))
    closest = seq[0]
    for i in range(1, n):
        closest = closest if decimalize(abs(closest - r)).compare(decimalize(abs(seq[i] - r))) <= 0 else seq[i]
    print(format(closest, standard))
