#!/usr/bin/python3
"""
Matrix Module
"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix.
    """
    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (matrix is None) or (len(matrix) == 0) or (type(matrix) is not list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for value in row:
            if (type(value) is not int) and (type(value) is not float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return (list(map(lambda row: (list(map(lambda value:
            round(value / div, 2), row))), matrix)))
