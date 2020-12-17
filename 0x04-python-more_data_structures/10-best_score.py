#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        maxx = max(values)
        pos = values.index(maxx)
        return keys[pos]
    else:
        return None
