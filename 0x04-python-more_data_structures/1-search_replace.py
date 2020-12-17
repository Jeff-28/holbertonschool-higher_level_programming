#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list:
        new = []
        for value in my_list:
            new.append(value if value != search else replace)
        return new
