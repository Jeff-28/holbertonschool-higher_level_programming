#!/usr/bin/python3
"""
I/O Module
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student with
        specified attributes"""
        if attrs is None:
            return self.__dict__
        new = {}
        for a in attrs:
            try:
                new[a] = self.__dict__[a]
            except:
                pass
        return new

    def reload_from_json(self, json):
        """Replaces all attributes of the Student"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
