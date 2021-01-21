#!/usr/bin/python3
"""
Inheritance Module
"""


def add_attribute(self, attr, value):
    """Adds a new attribute to an object if it’s possible"""

    if hasattr(self, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(self, attr, value)
