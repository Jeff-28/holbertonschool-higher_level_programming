#!/usr/bin/python3
"""Module contains find_peak(list_of_integers) function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    for idx in range(len(list_of_integers)):
        if list_of_integers[idx] > list_of_integers[idx - 1] and \
                list_of_integers[idx] > list_of_integers[idx + 1]:
            return list_of_integers[idx]
        if idx == len(list_of_integers) - 1:
            return list_of_integers[idx]
