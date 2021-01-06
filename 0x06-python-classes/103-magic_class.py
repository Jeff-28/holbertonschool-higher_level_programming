#!/usr/bin/python3
import math
"""MagicClass Module"""


class MagicClass:
    """MagicClass class"""
    def __init__(self, radius=0):
        """Takes radius as parameter."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference."""
        return 2 * math.pi * self.__radius
