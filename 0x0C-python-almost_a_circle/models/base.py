#!/usr/bin/python3
"""
Base Module
"""


class Base:
    """Manages id attributes in all future classes and
    to avoid duplicating the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
