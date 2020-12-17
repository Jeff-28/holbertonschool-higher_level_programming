#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        num = 0
        w = 0
        for tup in my_list:
            num += tup[0] * tup[1]
            w += tup[1]
        return num / w
    else:
        return 0
