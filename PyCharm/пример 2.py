#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from timeit import timeit

class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    Эта программа показыает работу декоратора, который производит оптимизацию
    хвостового вызова. Он делает это, вызывая исключение, если оно является его
    прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.
    Эта функция не работает, если функция декоратора не использует хвостовой вызов.
    """

    def func(*args, **kwargs):
        f = sys._getframe()
        if (f.f_back and f.f_back.f_back and
                f.f_back.f_back.f_code == f.f_code):
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def factorial(n, acc=1):
    """calculate a factorial"""
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


@tail_call_optimized
def fib(i, current=0, nxt=1):
    if i == 0:
        return current
    else:
        return fib(i - 1, nxt, current + nxt)


if __name__ == '__main__':
    n = 30
    setup1 = """from __main__ import factorial"""
    setup2 = """from __main__ import fib"""
    timer = timeit(stmt=f'factorial({n})', number=10, setup=setup1)
    print(f"Время выполнения функции factorial(): {timer}")
    timer = timeit(stmt=f'fib({n})', number=10, setup=setup2)
    print(f"Время выполнения функции fib(): {timer}")