#!/usr/bin/python3
"""
Base Module
"""

import json
import csv


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
        j_file = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for i in range(len(list_objs)):
                text.append(cls.to_dictionary(list_objs[i]))
        with open(j_file, 'w') as myfile:
            myfile.write(cls.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

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
        j_file = "{}.json".format(cls.__name__)
        try:
            with open(j_file, 'r') as myfile:
                lista = cls.from_json_string(myfile.read())
                instances = []
                for i in range(len(lista)):
                    instances.append(cls.create(**lista[i]))
        except:
            instances = []
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Has the same behavior as the JSON serialization/deserialization"""
        csv_file = cls.__name__ + ".csv"
        with open(csv_file, 'w', newline='') as myfile:
            writer = csv.writer(myfile)
            for obj in list_objs:
                if cls.__name__ is "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                    obj.y])
                elif cls.__name__ is "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Has the same behavior as the JSON serialization/deserialization"""
        csv_file = cls.__name__ + ".csv"
        lista = []
        try:
            with open(csv_file, newline='') as myfile:
                reader = csv.reader(myfile)
                for row in reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(row[1]),
                                      "height": int(row[2]), "x": int(row[3]),
                                      "y": int(row[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(row[0]), "size": int(row[1]),
                                      "x": int(row[2]), "y": int(row[3])}
                    obj = cls.create(**dictionary)
                    lista.append(obj)
        except:
            pass
        return lista
