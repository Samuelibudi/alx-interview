#!/usr/bin/python3

""" A method that returns a list of lists of integers
    representing the Pascal's triangle"""


def pascal_triangle(n):
    if n <= 0:
        return lst

    lst = [[1]]

    for m in range(1, n):
        row = [1]
        for i in range(1, m):
            row.append(lst[m-1][i-1] + lst[m-1][i])
        row.append(1)
        lst.append(row)
    return lst
