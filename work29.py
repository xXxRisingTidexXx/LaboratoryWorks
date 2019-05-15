"""
Лабораторна робота №29
ІПЗ - 12, Петраківський Данило
"""
from math import hypot, sqrt


class TDate:
    day = 1
    month = 1
    year = 1

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self):
        return self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0


class TPoint:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class TTriangle:
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return length(self.a, self.b) + length(self.b, self.c) + length(self.c, self.a)

    def square(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - length(self.a, self.b)) * (p - length(self.b, self.c)) * (p - length(self.c, self.a)))


def length(p1, p2):
    return hypot(p2.x - p1.x, p2.y - p1.y)


def pperimeter(points):
    perimeter = 0
    for i in range(len(points) - 1):
        perimeter += length(points[i], points[i + 1])
    return perimeter


def is_leap_year():
    """
    #1
    """
    for i in range(5):
        print('Введіть {} дату:'.format(i + 1))
        print(TDate(int(input('День: ')), int(input('Місяць: ')), int(input('Рік: '))).is_leap_year())


def calc_segment_length():
    """
    #2
    """
    a = TPoint(float(input('A.x: ')), float(input('A.y: ')))
    b = TPoint(float(input('B.x: ')), float(input('B.y: ')))
    c = TPoint(float(input('C.x: ')), float(input('C.y: ')))
    d = TPoint(float(input('D.x: ')), float(input('D.y: ')))
    print('|AB|: {}'.format(length(a, b)))
    print('|AC|: {}'.format(length(a, c)))
    print('|AD|: {}'.format(length(a, d)))


def calc_triangle_perimeter():
    """
    #3
    """
    a = TPoint(float(input('A.x: ')), float(input('A.y: ')))
    b = TPoint(float(input('B.x: ')), float(input('B.y: ')))
    c = TPoint(float(input('C.x: ')), float(input('C.y: ')))
    d = TPoint(float(input('D.x: ')), float(input('D.y: ')))
    print('P(ABC): {}'.format(TTriangle(a, b, c).perimeter()))
    print('P(ABD): {}'.format(TTriangle(a, b, d).perimeter()))
    print('P(ACD): {}'.format(TTriangle(a, c, d).perimeter()))


def calc_triangle_square():
    """
    #4
    """
    a = TPoint(float(input('A.x: ')), float(input('A.y: ')))
    b = TPoint(float(input('B.x: ')), float(input('B.y: ')))
    c = TPoint(float(input('C.x: ')), float(input('C.y: ')))
    d = TPoint(float(input('D.x: ')), float(input('D.y: ')))
    print('S(ABC): {}'.format(TTriangle(a, b, c).square()))
    print('S(ABD): {}'.format(TTriangle(a, b, d).square()))
    print('S(ACD): {}'.format(TTriangle(a, c, d).square()))


def calc_polygon_perimeter():
    """
    #5
    """
    for i in range(3):
        n = int(input('Введіть n: '))
        print('P: {}'.format(pperimeter(
            [TPoint(float(input('p[{}].x: '.format(j + 1))),
                    float(input('p[{}].y: '.format(j + 1)))) for j in range(n)]
        )))
