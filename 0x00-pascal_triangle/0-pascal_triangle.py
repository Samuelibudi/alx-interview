#!/usr/bin/python3

""" A method that returns a list of lists of integers
    representing the Pascal's triangle"""


def pascal_triangle(n):
    """
    Function to generate Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows of Pascal's Triangle.

    Returns:
    pascal_triangle (list): Pascal's Triangle as a list of lists of integers.
    """
    lst = []

    if n <= 0:
        return lst

    for i in range(n):
        row = [1]

        if i > 0:
            row.append(1)

        for j in range(1, i):
            row.append(lst[i - 1][j - 1] + lst[i - 1][j])
        lst.append(row)

    return lst
