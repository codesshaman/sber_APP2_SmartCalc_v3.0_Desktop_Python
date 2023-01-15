import math
import sympy as smp


def dot_find(value):
    return value.find(".")


def types_convert(value):
    if dot_find(value) == -1:
        return int(value)
    else:
        return float(value)


def math_eval(value):
    return eval(value)


def math_pi():
    return math.pi


def math_e():
    return math.e


def math_ln(value):
    return math.log(types_convert(value))


def math_log(value):
    return math.log10(types_convert(value))


def math_sin(value):
    return math.sin(types_convert(value))


def math_asin(value):
    return math.asin(types_convert(value))


def math_cos(value):
    return math.cos(types_convert(value))


def math_acos(value):
    return math.acos(types_convert(value))


def math_tan(value):
    return math.tan(types_convert(value))


def math_atan(value):
    return math.atan(types_convert(value))


def math_sqrt(value):
    return smp.sqrt(types_convert(value))


def math_power(value):
    return pow(types_convert(value), 2)