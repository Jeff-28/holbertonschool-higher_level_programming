#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new = a_dictionary
    keys = []
    for key, val in new.items():
        if val == value:
            keys.append(key)
    for x in keys:
        del new[x]
    return new
