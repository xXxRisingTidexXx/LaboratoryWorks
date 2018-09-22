"""
Лабораторна робота №11
ІПЗ - 12, Петраківський Данило
"""


def transform_1():
    """
    #1
    """
    n = int(input())
    s = input()
    s_length = len(s)
    print(s[s_length - n::] if s_length >= n else '.' * (n - s_length) + s)


def transform_2():
    """
    #2
    """
    n1 = int(input())
    n2 = int(input())
    s1 = input()
    s2 = input()
    print(s1[:n1] + s2[(len(s2) - n2):])


def extract_word():
    """
    #3
    """
    s = input()
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
    s = input()
    print(s[s.rindex('/') + 1:s.rindex('.')])


def extract_extension():
    """
    #5
    """
    s = input()
    print(s[s.rindex('.') + 1:])


def encrypt_1():
    """
    #6
    """
    text = input()
    encrypted_text = ''
    for ch in text:
        encrypted_text += chshift(ch) if ch.isalpha() else ch
    print(encrypted_text)


def chshift(ch, shift=1):
    encr = ord(ch) + shift
    return (chr(encr) if encr <= 90 else chr(encr - 26)) if ch.isupper() \
        else (chr(encr) if encr <= 122 else chr(encr - 26))


def encrypt_2():
    """
    #7
    """
    text = input()
    k = int(input())
    encrypted_text = ''
    for ch in text:
        encrypted_text += chshift(ch, shift=k) if ch.isalpha() else ch
    print(encrypted_text)
