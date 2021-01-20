#!/usr/bin/python3
"""
MyInt Module
"""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __new__(cls, *args, **kwargs):
        """Creates new instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """== is now !="""
        return int(self) != other

    def __ne__(self, other):
        """!= is now =="""
        return int(self) == other
