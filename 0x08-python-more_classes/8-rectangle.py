#!/usr/bin/python
"""
Rectangle Module - creates and defines rectangles.
"""

class Rectangle:
    """A class to work with Rectangle objects."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates a new object."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the attribute width."""
        return self.__width
    @width.setter
    def width(self, value):
        """Defines the width with the value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the attribute height."""
        return self.__height
    @height.setter
    def height(self, value):
        """Defines the height with the value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """Returns the object representation in string format."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        """Returns a string representation of the object."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_str = ((str(self.print_symbol) * self.__width) + "\n") * self.__height
        return rec_str[:-1]

    def __del__(self):
        """Prints message when instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle."""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
