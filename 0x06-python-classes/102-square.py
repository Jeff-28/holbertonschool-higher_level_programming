#!/usr/bin/python3
"""
Square Module - creates and defines the square class.
"""


class Square:
    """A new class created for an object oriented programming
        project. It takes the size argument."""

    def __init__(self, size=0):
        """Defines the private attribute size."""
        self.size = size

    @property
    def size(self):
        """Returns the private attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines the private attribute size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        return (self.size == other.size)

    def __ne__(self, other):
        return (self.size != other.size)

    def __lt__(self, other):
        return (self.size < other.size)

    def __gt__(self, other):
        return (self.size > other.size)

    def __le__(self, other):
        return (self.size <= other.size)

    def __ge__(self, other):
        return (self.size >= other.size)
