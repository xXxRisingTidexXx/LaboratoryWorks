"""
Лабораторна робота №27
ІПЗ - 12, Петраківський Данило
"""
from re import match, split


def check_identifier():
    """
    #1
    """
    for i in range(5):
        print(check(input('Введіть s: ')))


def check(s):
    return 0 if match(r'^[A-Za-z_]\w*$', s) else -1 if s == '' else \
            -2 if match('^\d', s) else s.index(match(r'^\w*(\W)', s)[1])


def invert_string():
    """
    #2
    """
    s = input('Введіть s: ')
    for i in range(3):
        print('Інвертований рядок: {}'.format(
            invert(s, int(input('Введіть k[{}]: '.format(i))), int(input('Введіть n[{}]: '.format(i))))
        ))


def invert(s, k, n):
    length = len(s)
    return '' if k > length else s[:k] + s[:k - 1:-1] if k + n > length else s[:k] + s[k + n - 1:k - 1:-1] + s[k + n:]


def extract_word():
    """
    #3
    """
    s = input('Введіть s: ')
    for i in range(3):
        print('k-те слово: {}'.format(extract(s, int(input('Введіть k[{}]: '.format(i))))))


def extract(s, k):
    w = words(s)
    return '' if k > len(w) else w[k - 1]


def words(s):
    w = split(r'\W+', s)
    if '' in w:
        w.remove('')
    return w


def create_word_list():
    """
    #4
    """
    s = input('Введіть s: ')
    wl = word_list(s)
    print('n: {}, w: {}'.format(wl[0], wl[1]))


def word_list(s):
    w = words(s)
    return len(w), w


def compress_string():
    """
    #5
    """
    for i in range(5):
        print('Стиснутий рядок: {}'.format(compress(input('Введіть s: '))))


def compress(s):
    if len(s) < 3:
        return s
    cs = ''
    i = 0
    repetition = s[i]
    length = len(s)
    for j in range(1, length, 1):
        if repetition[0] != s[j]:
            cs += simplify(repetition, s, i, j)
            i = j
            repetition = ''
        repetition += s[j]
    cs += simplify(repetition, s, i, length)
    return cs


def simplify(repetition, s, i, j):
    rlen = len(repetition)
    return '%s{%d}' % (repetition[0], rlen) if rlen >= 3 else s[i:j]


def decimal_to_binary():
    """
    #6
    """
    for i in range(5):
        print('Двійкове представлення n: {}'.format(dec_to_bin(int(input('Введіть n: ')))))


def dec_to_bin(n):
    return bin(n)[2:]


def decimal_to_hexadecimal():
    """
    #7
    """
    for i in range(5):
        print('Шістнадцяткове представлення n: {}'.format(dec_to_hex(int(input('Введіть n: ')))))


def dec_to_hex(n):
    return hex(n)[2:]


def binary_to_decimal():
    """
    #8
    """
    for i in range(5):
        print('Десяткове представлення s: {}'.format(bin_to_dec(input('Введіть s: '))))


def bin_to_dec(n):
    return int(n, base=2)


def hexadecimal_to_decimal():
    """
    #9
    """
    for i in range(5):
        print('Десяткове представлення s: {}'.format(hex_to_dec(input('Введіть s: '))))


def hex_to_dec(n):
    return int(n, base=16)
