"""
Лабораторна робота №1
ІПЗ - 12, Петраківський Данило
"""
from random import randint


def perform_arithmetical_operations():
    """
    #1
    """
    a = int(input('Перше число: '))
    b = int(input('Друге число: '))
    print(a * b)


def draw_text_picture():
    """
    #2
    """
    print('\n   /~~~\\   \n  //^ ^\\\\  \n (/(_&_)\\) \n _/\'\'*\'\'\\_ \n (/_)^(_\\) \n')


def input_tricky_text():
    """
    #3
    """
    s1 = input('Суб\'єкт: ')
    s2 = input('Дія: ')
    s3 = input('Об\'єкт: ')
    s1_length = len(s1)
    s2_length = len(s2)
    print('{}\n{}\n{}'.format(s1, ' ' * s1_length + s2, ' ' * (s1_length + s2_length) + s3))


def output_tournament_winners():
    """
    #4
    """
    name_1 = input('3 місце: ')
    name_2 = input('2 місце: ')
    name_3 = input('1 місце: ')
    place_1 = '__{}__'.format(name_3)
    place_2 = '|__{}__'.format(name_2)
    place_3 = '|__{}__'.format(name_1)
    place_1_length = len(place_1)
    place_2_length = len(place_2)
    place_3_length = len(place_3)
    tab_1 = place_1_length // 2
    tab_2 = place_2_length // 2
    tab_3 = place_3_length // 2
    s2 = '{}1{}{}'.format(' ' * tab_1, ' ' * (tab_1 + place_1_length % 2 - 1), place_2)
    s3 = '{}2{}{}'.format(' ' * (place_1_length + tab_2), ' ' * (tab_2 + place_2_length % 2 - 1), place_3)
    s4 = '{}3{}|'.format(' ' * (len(s2) + tab_3), ' ' * (tab_3 - 2 + place_3_length % 2))
    print(place_1, s2, s3, s4, sep='\n')


def dice():
    """
    #5
    """
    a = randint(1, 6)
    b = randint(1, 6)
    print('1-а кість: {}'.format(a))
    print('2-а кість: {}'.format(b))
    print('Сума очок: {}'.format(a + b))
