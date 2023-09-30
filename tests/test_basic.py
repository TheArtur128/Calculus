from functools import partial
from typing import Callable
from operator import add

from calculus.basic import *


def number_of(func: Callable[Callable[int, int], Callable[int, int]]) -> int:
    return func(partial(add, 1))(0)


def test_NOT() -> None:
    assert NOT(TRUE) is FALSE
    assert NOT(FALSE) is TRUE


def test_AND() -> None:
    assert AND(TRUE)(TRUE) is TRUE
    assert AND(FALSE)(FALSE) is FALSE
    assert AND(TRUE)(FALSE) is FALSE
    assert AND(FALSE)(TRUE) is FALSE


def test_OR() -> None:
    assert OR(TRUE)(TRUE) is TRUE
    assert OR(FALSE)(FALSE) is FALSE
    assert OR(TRUE)(FALSE) is TRUE
    assert OR(FALSE)(TRUE) is TRUE


def test_XOR() -> None:
    assert XOR(TRUE)(TRUE) is FALSE
    assert XOR(FALSE)(FALSE) is FALSE
    assert XOR(TRUE)(FALSE) is TRUE
    assert XOR(FALSE)(TRUE) is TRUE


def test_INCERENTED() -> None:
    assert number_of(INCERENTED(_0)) == 1
    assert number_of(INCERENTED(_1)) == 2
    assert number_of(INCERENTED(_2)) == 3
    assert number_of(INCERENTED(_3)) == 4
    assert number_of(INCERENTED(_4)) == 5
    assert number_of(INCERENTED(_5)) == 6
    assert number_of(INCERENTED(_6)) == 7
    assert number_of(INCERENTED(_7)) == 8
    assert number_of(INCERENTED(_8)) == 9
    assert number_of(INCERENTED(_9)) == 10
    assert number_of(INCERENTED(_10)) == 11


def test_PLUS() -> None:
    assert number_of(PLUS(_0)(_0)) == 0
    assert number_of(PLUS(_2)(_5)) == 7
    assert number_of(PLUS(_5)(_2)) == 7
    assert number_of(PLUS(_10)(_10)) == 20


def test_MUL() -> None:
    assert number_of(MUL(_0)(_0)) == 0
    assert number_of(MUL(_0)(_5)) == 0
    assert number_of(MUL(_5)(_0)) == 0
    assert number_of(MUL(_2)(_5)) == 10
    assert number_of(MUL(_5)(_2)) == 10
    assert number_of(MUL(_10)(_10)) == 100


def test_POW() -> None:
    assert number_of(POW(_0)(_5)) == 0
    assert number_of(POW(_4)(_1)) == 4
    assert number_of(POW(_2)(_2)) == 4
    assert number_of(POW(_2)(_4)) == 16
    assert number_of(POW(_2)(_8)) == 256


def test_PAIR() -> None:
    assert LEFT_OF(PAIR(TRUE)(FALSE)) is TRUE
    assert RIGHT_OF(PAIR(TRUE)(FALSE)) is FALSE


def test_DECREMENTED() -> None:
    assert number_of(DECREMENTED(_3)) == 2
    assert number_of(DECREMENTED(_0)) == 0


def test_MINUS() -> None:
    assert number_of(MINUS(_3)(_2)) == 1
    assert number_of(MINUS(_3)(_0)) == 3
    assert number_of(MINUS(_10)(_6)) == 4


def test_IF() -> None:
    assert IF(TRUE)(True)(False)
    assert IF(FALSE)(False)(True)
    assert IF(_0)(False)(True)


def test_IS_ZERO() -> None:
    assert IS_ZERO(_0) is TRUE
    assert IS_ZERO(_1) is FALSE
    assert IS_ZERO(_8) is FALSE


def test_LE() -> None:
    assert LE(_0)(_0) is TRUE
    assert LE(_2)(_3) is TRUE
    assert LE(_2)(_2) is TRUE
    assert LE(_3)(_2) is FALSE


def test_LT() -> None:
    assert LT(_0)(_0) is TRUE
    assert LT(_2)(_3) is TRUE
    assert LT(_2)(_2) is FALSE
    assert LT(_3)(_2) is FALSE


def test_EQ() -> None:
    assert EQ(_0)(_0) is TRUE
    assert EQ(_2)(_3) is FALSE
    assert EQ(_2)(_2) is TRUE
    assert EQ(_3)(_2) is FALSE


def test_DIV() -> None:
    assert number_of(DIV(_4)(_2)) == 2
    assert number_of(DIV(_4)(_4)) == 1
    assert number_of(DIV(_4)(_8)) == 0
