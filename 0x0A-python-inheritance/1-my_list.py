#!/usr/bin/python3
"""
MyList Module
"""


class MyList(list):
    """Inherits from class list"""

    def print_sorted(self):
        """Prints the list sorted"""
        super().__str__()
        print(sorted(self))
