"""
Лабораторна робота №10
ІПЗ - 12, Петраківський Данило
"""
from work_8 import standard


def make_snapshots():
    """
    #1
    """
    name = input()
    name_length = len(name)
    print(name[2])
    print(name[name_length - 2])
    print(name[:5])
    print(name[:name_length - 2])
    print(name[::2])
    print(name[1::2])
    print(name[::-1])
    print(name[::-2])
    print(name_length)


def trim():
    """
    #2
    """
    lexemes = input().replace('    ', ' '). replace('   ', ' ').replace('  ', ' ').split()
    word_count = 0
    for lexeme in lexemes:
        word_count += check_lexeme(lexeme)
    print(word_count)


def check_lexeme(lexeme):
    for c in lexeme:
        if c.isalpha():
            return 1
    return 0


def swap_name_and_surname():
    """
    #3
    """
    names = input().split()
    print('{} {}'.format(names[1], names[0]))


def divide_name():
    """
    #4
    """
    name = input()
    name_length = len(name)
    half = name[:name_length // 2 + name_length % 2]
    print(name.replace(half, ''), half, sep='')


def remove_third_chars():
    """
    #5
    """
    text = 'In the hole in the ground there lived a hobbit.'
    new_text = ''
    for i in range(len(text)):
        new_text += '' if i % 3 == 0 else text[i]
    print(new_text)


def format_full_name():
    """
    #6
    """
    full_name = input().split()
    print('{} {}.{}.'.format(full_name[2].capitalize(), full_name[0][0].capitalize(), full_name[1][0].capitalize()))


def calc_expression():
    """
    #7
    """
    lex = input().split()
    ops = {'*': lambda x, y: float(x) * float(y), '/': lambda x, y: float(x) / float(y),
           '+': lambda x, y: float(x) + float(y), '-': lambda x, y: float(x) - float(y)}
    priority = is_prioritized(lex[1])
    if priority or not (priority or is_prioritized(lex[3])):
        res = ops[lex[3]](ops[lex[1]](lex[0], lex[2]), lex[4])
    else:
        res = ops[lex[1]](lex[0], ops[lex[3]](lex[2], lex[4]))
    print(format(res, standard))


def is_prioritized(operation):
    return operation == '*' or operation == '/'
