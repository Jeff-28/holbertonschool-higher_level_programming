#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        flag = 0
        for j in i:
            if flag == len(i) - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d} ".format(j), end="")
            flag += 1
        else:
            print()
