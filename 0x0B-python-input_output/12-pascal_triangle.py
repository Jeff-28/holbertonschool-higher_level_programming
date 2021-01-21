#!/usr/bin/python3
"""
12-main
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    pascal = []
    if n <= 0:
        return pascal
    new_list = [1]
    i = 0
    while i < n:
        pascal.append(new_list)
        temp = new_list[:]
        temp.append(0)
        idx = 1
        for x in new_list:
            temp[idx] += x
            idx += 1
        new_list = temp
        i += 1
    return pascal
