#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)
    if size1 == 0:
        list1 = list(tuple_a)
        list1.append(0)
        list1.append(0)
        tuple_a = tuple(list1)
    if size1 == 1:
        list1 = list(tuple_a)
        list1.append(0)
        tuple_a = tuple(list1)

    if size2 == 0:
        list2 = list(tuple_b)
        list2.append(0)
        list2.append(0)
        tuple_b = tuple(list2)
    if size2 == 1:
        list2 = list(tuple_b)
        list2.append(0)
        tuple_b = tuple(list2)
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
