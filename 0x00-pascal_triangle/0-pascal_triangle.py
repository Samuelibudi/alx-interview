#!/usr/bin/python3

""" A method that returns a list of lists of integers
    representing the Pascal's triangle"""

import math


def pascal_triangle(n):
    lst = []
    if n <= 0:
        return lst

    for m in range(n):
        lst.append([])
        for i in range(m+1):
            lst[m].append(math.comb(m, i))
    return lst
