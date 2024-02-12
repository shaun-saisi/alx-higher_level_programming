#!/usr/bin/python3
"""Basic square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A square inheriting from a class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ the constructor to initialize the square

        Args:
            size: the size of the square
            x: The x coordinate
            y: the y coordinate
            id: the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is not None:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is not None:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
 
