"""
Лабораторна робота №11
ІПЗ - 12, Петраківський Данило
"""


def transform_1():
    """
    #1
    """
    n = int(input('Введіть n: '))
    s = input('Введіть s: ')
    s_length = len(s)
    print(s[s_length - n::] if s_length >= n else '.' * (n - s_length) + s)


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
    if s.count(' ') <= 1:
        print('')
    else:
        s = s[s.index(' '):]
        print(s)
        print(s[:s.index(' ') + 1])


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
    encr = ord(ch) + shift
    return chr(encr) if encr <= 90 else chr(encr - 26) if ch.isupper() \
        else (chr(encr) if encr <= 122 else chr(encr - 26))


def encrypt_2():
    """
    #7
    """
    text = input('Введіть текст: ')
    k = int(input('Введіть k: '))
    print(''.join([chshift(ch, shift=k) if ch.isalpha() else ch for ch in text]))
