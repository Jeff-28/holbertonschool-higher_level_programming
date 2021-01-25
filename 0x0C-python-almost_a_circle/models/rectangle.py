#!/usr/bin/python3
"""
Rectangle Module
"""

Base = __import__("base").Base


class Rectangle(Base):
    """Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines the attribute with the value"""
        self.__width = value

    @property
    def height(self):
        """Returns the attribute"""
        return self.__heigth

    @height.setter
    def height(self, value):
        """Defines the attribute with the value"""
        self.__height = value

    @property
    def x(self):
        """Returns the attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Defines the attribute with the value"""
        self.__x = value

    @property
    def y(self):
        """Returns the attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Defines the attribute with the value"""
        self.__y = value
