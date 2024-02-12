#!/usr/bin/python3

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

