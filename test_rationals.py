from pytest import raises
from rationals import Rational as R


def test_bad_rationals():
    with raises(RuntimeError):
        R()
    with raises(RuntimeError):
        R(-0, 0)
    with raises(RuntimeError):
        R(-4, 0)
    with raises(RuntimeError):
        R('-4/0')
    with raises(RuntimeError):
        R('')
    with raises(RuntimeError):
        R('0/0')
    with raises(RuntimeError):
        R('ytyuuiioopp[ojhg')
    with raises(RuntimeError):
        R('y/6')
    with raises(RuntimeError):
        R('-7/dfrt')
    with raises(RuntimeError):
        R('-3/-6')
    with raises(RuntimeError):
        R(3) / R(0)
    with raises(RuntimeError):
        R('0') / R('0')
    with raises(RuntimeError):
        R(3, 0) / R(0, 6)


def test_rationals_creation():
    assert str(R(2, 3)) == '2/3'
    assert str(R(2, 1)) == '2'
    assert str(R(2, 4)) == '1/2'
    assert str(R(9, 3)) == '3'
    assert str(R(-8, -3)) == '8/3'
    assert str(R(-13, 7)) == '-13/7'
    assert str(R(1024, 32)) == '32'
    assert str(R(63, -18)) == '-7/2'
    assert str(R(128)) == '128'
    assert str(R(-4)) == '-4'
    assert str(R(0)) == '0'
    assert str(R('0')) == '0'
    assert str(R('9')) == '9'
    assert str(R('-17')) == '-17'
    assert str(R('-1/1')) == '-1'
    assert str(R('13/18')) == '13/18'
    assert str(R('-62/93')) == '-2/3'
    assert str(R('-15/3')) == '-5'
    assert str(R('17/1')) == '17'
    assert str(R('0/1')) == '0'
    assert str(R(0, 18)) == '0'


def test_comparison():
    assert R(3, 5) == R(6, 10)
    assert R(-2, -6) == R('1/3')
    assert R('8/14') == R(-4, -7)
    assert R('21/35') == R(3, 5)
    assert R('90/18') < R(6)
    assert R('12/3') >= -R(-4)
    assert R(0) != R('12/13')
    assert R(6, 7) > R('5/6')
    assert R(18) <= -R('-72/4')


def test_addition():
    assert R(2, 3) + R(4, 3) == R(2)
    assert R(1) + R(-5) == R(-8, 2)
    assert R(1) + R(-5) == R(-8, 2)
    assert R(1, 7) + R(-5, 3) == R(-32, 21)
    assert R('3') + R('-5') == R('-2')
    assert R('0') + R('-5/2') == R('-5/2')
    assert R('6') + R('12/4') == R('9')
    assert R('5/9') + R('13/14') == R('187/126')
    assert R('6/9') + R('-13/12') == R('-15/36')
    assert R('-2/7') + R('-12/7') == R('-2')


def test_negation():
    assert -R(3, 4) == R(-3, 4)
    assert -R(19) == R(-19)
    assert -R(26, 13) == R(-2)
    assert -R('13/18') == R('-13/18')
    assert -R('29') == R(-29)
    assert -R('-36/45') == R(4, 5)


def test_subtraction():
    assert R(3, 4) - R(1, 2) == R(1, 4)
    assert R('15/3') - R('4/2') == R('9/3')
    assert R('2/6') - R('3/9') == R('0')
    assert R('8/9') - R('-1/15') == R('43/45')
    assert R('5') - R('5') == R('0')
    assert R('0') - R('0/5') == R(0)
    assert R('3/8') - R('-5/8') == R('1')


def test_multiplication():
    assert R(0) * R(0) == R(0)
    assert R(0) * R(5) == R(0)
    assert R(5) * R(0) == R(0)
    assert R(5) * R(-5) == R(-25)
    assert R('5') * R('-5') == R('-25')
    assert R('18/9') * R('-5/3') == R('-10/3')
    assert R('5/7') * R('2/13') == R('10/91')
    assert R('-5/7') * R('7/5') == R('-1')
    assert R('11/12') * R('12/13') == R('11/13')


def test_division():
    assert R(0) / R(5) == R(0)
    assert R(-5) / R(5) == R(-1)
    assert R(1) / R(1907) == R('1/1907')
    assert R('6/9') / R('36/12') == R('2/9')
    assert R('-5/16') / R('2/9') == R('-45/32')


def test_operators():
    assert R('22/9') * R('9/4') - R('56/9') * R('3/8') == R('19/6')
    assert (R('5/7') + R('3/14')) / R('20/7') == R('13/40')
    assert R('3/2') * R('3/2') * R('3/2') * (R('7/9') - R('2/3')) == R('3/8')
    assert (R('14/3') + R('7/6')) / R('5') == R('7/6')
    assert (R('23/2') + R('69/2')) / (R('5/4') + R('9/2')) == R('8')
