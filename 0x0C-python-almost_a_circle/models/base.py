#!/usr/bin/python3
"""
Base Module
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        text = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                text.append(cls.to_dictionary(list_objs[i]))
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as myfile:
            myfile.write(cls.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__), 'r') as myfile:
                lista = cls.from_json_string(myfile.read())
                instances = []
                for i in range(len(lista)):
                    instances.append(cls.create(**lista[i]))
        except:
            instances = []
        return instances
