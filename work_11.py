"""
Лабораторна робота №11
ІПЗ - 12, Петраківський Данило
"""
from re import match


def transform_1():
    """
    #1
    """
    n = int(input('Введіть n: '))
    s = input('Введіть s: ')
    slen = len(s)
    print(s[slen - n::] if slen >= n else '.' * (n - slen) + s)


def transform_2():
    """
    #2
    """
    n1 = int(input('Введіть n1: '))
    n2 = int(input('Введіть n2: '))
    s1 = input('Введіть s1: ')
    s2 = input('Введіть s2: ')
    print(s1[:n1] + s2[(len(s2) - n2):])


def extract_word():
    """
    #3
    """
    s = input('Введіть s: ')
    print('' if s.count(' ') <= 1 else match(r'\S+ (\S+) \S+', s).groups()[0])


def extract_filename():
    """
    #4
    """
    s = input('Введіть s: ')
    print(s[s.rindex('/') + 1:s.rindex('.')])


def extract_extension():
    """
    #5
    """
    s = input('Введіть s: ')
    print(s[s.rindex('.') + 1:])


def encrypt_1():
    """
    #6
    """
    text = input('Введіть текст: ')
    print(''.join([chshift(ch) if ch.isalpha() else ch for ch in text]))


def chshift(ch, shift=1):
    code = ord(ch) + shift
    return chr(code) if ch.isupper() and code <= 90 or ch.islower() and code <= 122 else chr(code - 26)


def encrypt_2():
    """
    #7
    """
    k = int(input('Введіть k: '))
    text = input('Введіть текст: ')
    print(''.join([chshift(ch, shift=k) if ch.isalpha() else ch for ch in text]))
