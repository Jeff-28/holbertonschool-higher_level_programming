#!/usr/bin/python3
"""
LockedClass Module
"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes."""

    def __setattr__(self, attribute, value):
        """Sets attribute only if the new instance attribute is called
        first_name."""
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")

