#!/usr/bin/python3
"""
Square Module - creates and defines the square class.
"""


class Square:
    """A new class created for an object oriented programming
        project. It takes the size argument."""

    def __init__(self, size=0, position=(0, 0)):
        """Defines the private attribute size."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the attribute position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Defines the position."""
        if type(value) is tuple and type(value[0]) is int and value[0] >= 0\
                and type(value[1]) is int and value[1] >= 0\
                and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for space in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print()

    def __repr__(self):
        """Returns the object representation in string format."""
        if self.__size == 0:
            return ("")
        else:
            rep = []
            for space in range(self.position[1]):
                rep.append('')
            for row in range(self.size):
                line = []
                for spaces in range(self.position[0]):
                    line.append(' ')
                for row in range(self.size):
                    line.append('#')
                rep.append(line)
            return ('\n'.join(map(lambda line: ''.join(line), rep)))
