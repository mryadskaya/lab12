#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_correct_brackets(string):

    if len(string) == 0:
        return True

    if string.count('(') != string.count(')'):
        return False

    index = string.index('(')
    pair_index = find_closing_bracket(string, index)

    if pair_index == -1:
        return False

    if not is_correct_brackets(string[index + 1: pair_index]):
        return False

    return is_correct_brackets(string[pair_index + 1:])

def find_closing_bracket(string, start):
    count = 0

    for i in range(start, len(string)):
        if string[i] == '(':
            count += 1
        elif string[i] == ')':
            count -= 1

        if count == 0:
            return i

    return -1


print(is_correct_brackets(input("Введите строку со скобками: ")))
