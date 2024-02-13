#!/usr/bin/python3

import json

"""Defines a base class"""

class Base:
    """The main class
    Args:
        __nb_objects = 0: The private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor
        Args:
            id: the id of the constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        """Return the json format of the strings

        Args:
            list_dictionaries: the list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod

    def save_to_file(cls, list_objs):
        """writes json string rep of list_objs
        
        Args:
            list_objs: a list of instances that inherits from base
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of json representation

        Args:
            json_string: string representing the list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args: 
            **dctionary: double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1,1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


