#!/usr/bin/python3
"""
Rectangle Module
"""

from models.base import Base


class Rectangle(Base):
    """Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines the attribute with the value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defines the attribute with the value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Defines the attribute with the value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Defines the attribute with the value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for blank in range(self.__y):
            print()
        for row in range(self.__height):
            for col in range(self.__width):
                if col == 0:
                    for blank in range(self.__x):
                        print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of an instance"""
        dictionary = {"id": 0, "width": 0, "height": 0, "x": 0, "y": 0}
        for key in dictionary:
            if key == "id":
                dictionary[key] = self.id
            if key == "width":
                dictionary[key] = self.width
            if key == "height":
                dictionary[key] = self.height
            if key == "x":
                dictionary[key] = self.x
            if key == "y":
                dictionary[key] = self.y
        return dictionary
