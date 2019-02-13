#!/usr/bin/env python

import math


def f(x):
    return math.e**x-2


def derivative(x):
    h = 0.000001
    return (f(x + h) - f(x)) / h


def newton_raphson(x):
    return x - (f(x) / derivative(x))


def iterate(x, n):
    for _ in range(n):
        x = newton_raphson(x)
    return x


def main():
    print(iterate(1, 10))  # prints 0.6931471805599454
    print(iterate(1, 100))  # prints 0.6931471805599454


if __name__ == '__main__':
    main()

