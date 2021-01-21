#!/usr/bin/python3
"""
I/O Module
"""

import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file" """

    with open(filename, encoding='utf-8') as myfile:
        return json.load(myfile)
