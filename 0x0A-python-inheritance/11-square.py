#!/usr/bin/python3
"""
Square Module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        """Instantiates a new object"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
