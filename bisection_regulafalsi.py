#!/usr/bin/env python

import numpy as np
import math


def f(x):
    return x**3-math.cos(x)-1


def bisection(a, b, tol):
    c = (a + b) / 2.0
    i = 0
    while (b - a) / 2.0 > tol:
        i = i + 1
        if f(c) == 0:
            return c, i
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c
        c = (a + b) / 2.0
    return c, i


def regulafalsi(a, b, tol):
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    i = 0
    while np.abs(f(c)) > tol:
        i = i + 1
        if f(c) == 0:
            return c, i
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    return c, i


def main():
    print(bisection(-3, 3, 10 ** -10))  # prints (1.1265619081968907, 35)
    print(regulafalsi(-3, 3, 10 ** -10))  # prints (1.1265619081322114, 65)


if __name__ == '__main__':
    main()

