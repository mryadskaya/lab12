#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import timeit
from functools import lru_cache

import sys

@lru_cache
def factorial_recursion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

@lru_cache
def fib_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursion(n - 2) + fib_recursion(n - 1)

def factorial_iterable(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

def fib_iterable(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    n = 35
    setup1 = """from __main__ import fib_recursion"""
    setup2 = """from __main__ import factorial_recursion"""
    timer = timeit(stmt=f'fib_recursion({n})', number=10, setup=setup1)
    print('Время выполнения рекурсивной функции c @lru_cache: ', {timer})
    timer = timeit(stmt=f'factorial_recursion({n})', number=10, setup=setup2)
    print('Время выполнения рекурсивной функции с @lru_cache: ', {timer})