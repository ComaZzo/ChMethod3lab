from math import sin, cos

from constances import *


def func_first(x: float, y: float) -> float:
    return 2 * x ** 2 - x * y - y ** 2 + 2 * x - 2 * y + 6


def func_second(x: float, y: float) -> float:
    return y * sin(y) - x - 1


def func_first_dx(x: float, y: float) -> float:
    return 4 * x - y + 2


def func_first_dy(x: float, y: float) -> float:
    return -x - 2 * (y + 1)


def func_second_dx(x: float, y: float) -> float:
    return -1


def func_second_dy(x: float, y: float) -> float:
    return sin(y) + y * cos(y)


def func_first_dx_ch(x: float, y: float) -> float:
    return (func_first(x + const_h, y) - func_first(x, y)) / const_h


def func_first_dy_ch(x: float, y: float) -> float:
    return (func_first(x, y + const_h) - func_first(x, y)) / const_h


def func_second_dx_ch(x: float, y: float) -> float:
    return (func_second(x + const_h, y) - func_second(x, y)) / const_h


def func_second_dy_ch(x: float, y: float) -> float:
    return (func_second(x, y + const_h) - func_second(x, y)) / const_h

