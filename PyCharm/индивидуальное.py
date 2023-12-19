#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def brackets_check(s):
    meetings = 0
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0


if __name__ == '__main__':
    if brackets_check(input('Введите строку: ')):
        print('True')
    else:
        print('False')