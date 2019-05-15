"""
Лабораторна робота №10
ІПЗ - 12, Петраківський Данило
"""
from re import compile

STANDARD = '.3f'


def make_snapshots():
    """
    #1
    """
    s = input('Введіть s: ')
    slen = len(s)
    print(s[2])
    print(s[slen - 2])
    print(s[:5])
    print(s[:slen - 2])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(slen)


def trim():
    """
    #2
    """
    pattern = compile(r'[A-Za-z]+')
    print(len(list(filter(
        lambda w: len(pattern.findall(w)) > 0,
        input('Введіть речення: ').replace('    ', ' '). replace('   ', ' ').replace('  ', ' ').split()
    ))))


def swap_name_and_surname():
    """
    #3
    """
    names = input('Введіть ім\'я та прізвище: ').split()
    print('{} {}'.format(names[1], names[0]))


def divide_name():
    """
    #4
    """
    name = input('Введіть ім\'я: ')
    nlen = len(name)
    half = name[:nlen // 2 + nlen % 2]
    print(name.replace(half, ''), half, sep='')


def remove_third_chars():
    """
    #5
    """
    text = 'In the hole in the ground there lived a hobbit.'
    print(''.join(['' if i % 3 == 0 else text[i] for i in range(1, len(text))]))


def format_full_name():
    """
    #6
    """
    full_name = input('Введіть ПІБ: ').split()
    print('{} {}.{}.'.format(full_name[2].capitalize(), full_name[0][0].capitalize(), full_name[1][0].capitalize()))


def calc_expression():
    """
    #7
    """
    exp = input('Введіть вираз: ').split()
    ops = {'*': lambda x, y: float(x) * float(y), '/': lambda x, y: float(x) / float(y),
           '+': lambda x, y: float(x) + float(y), '-': lambda x, y: float(x) - float(y)}
    print(format(ops[exp[1]](exp[0], ops[exp[3]](exp[2], exp[4]))
                 if not checkop(exp[1]) and checkop(exp[3]) else
                 ops[exp[3]](ops[exp[1]](exp[0], exp[2]), exp[4]), STANDARD))


def checkop(operation):
    return operation == '*' or operation == '/'
