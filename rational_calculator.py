from rationals import Rational as R


SIGNS = {
    '+': lambda x, y: x + y, '-': lambda x, y: x - y,
    '*': lambda x, y: x * y, '/': lambda x, y: x / y
}

ERROR = 'Incorrect input; try again.'

if __name__ == '__main__':
    print(
        'Welcome to RC. Here you can work with rational numbers. Mathematical '
        'operations (+, -, *, /) are allowed as well. Type "\\q" to exit. Good luck:)'
    )
    active, left, sign = True, None, None
    while active:
        cin = input()
        if cin == '\\q':
            active = False
            print('Goodbye:)')
        else:
            try:
                if left is None and sign is None:
                    left = R(cin)
                elif left is not None and sign is None:
                    sign = SIGNS[cin]
                else:
                    left = sign(left, R(cin))
                    sign = None
                    print(left)
            except (RuntimeError, KeyError):
                print(ERROR)
