#!/usr/bin/python3
"""
Module provides the following function:

    add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """Returns the sum of a and b.
    Where a and b should end up being integers,
    otherwise a TypeError shall raise."""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
