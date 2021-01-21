#!/usr/bin/python3
"""
I/O Module
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object"""

    return obj.__dict__
