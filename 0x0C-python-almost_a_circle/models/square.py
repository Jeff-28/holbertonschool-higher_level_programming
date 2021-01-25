#!/usr/bin/python3
"""
Square Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of instance"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """Returns the attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Defines the attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of an instance"""
        dictionary = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in dictionary:
            if key == "id":
                dictionary[key] = self.id
            if key == "size":
                dictionary[key] = self.width
            if key == "x":
                dictionary[key] = self.x
            if key == "y":
                dictionary[key] = self.y
        return dictionary
