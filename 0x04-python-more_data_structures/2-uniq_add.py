#!/usr/bin/python3


def uniq_add(my_list=[]):
    if len(my_list) != 0:
        result = 0
        for x in set(my_list):
            result += x
        return result
    else:
        return None
