#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(cols):
        for j in range(rows):
            if j == rows - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d} ".format(matrix[i][j]), end="")
        else:
            print()
