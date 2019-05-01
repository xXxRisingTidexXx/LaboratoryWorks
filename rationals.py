from re import compile
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


class Rational:
    __quotient_validator = compile(r'^(-?[1-9]\d*)/([1-9]\d*)$')

    def __init__(self, *args):
        try:
            if len(args) == 1:
                try:
                    quotient = self.__quotient_validator.match(args[0]).groups()
                    self.__m, self.__n = int(quotient[0]), int(quotient[1])
                    self.__try_reduce()
                except TypeError:
                    self.__m, self.__n = int(args[0]), 1
            elif len(args) == 2:
                self.__m, self.__n = int(args[0]), int(args[1])
                if self.__m == 0 or self.__n == 0:
                    raise ValueError()
                self.__try_negate()
                self.__try_reduce()
            else:
                raise ValueError()
        except ValueError:
            raise RuntimeError(f'{args} can\'t be converted into a rational number')

    def __try_reduce(self):
        divider = gcd(self.__m, self.__n)
        self.__m //= divider
        self.__n //= divider

    def __try_negate(self):
        if self.__n < 0:
            self.__m = -self.__m
            self.__n = -self.__n

    def __str__(self):
        return f'{self.__m}/{self.__n}' if self.__n != 1 else str(self.__m)

    def __eq__(self, other):
        return self.__m == other.__m and self.__n == other.__n

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.__m * other.__n > other.__m * self.__n

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other
