#!/usr/bin/python3

""" defining the class square"""

class Square:
    """What is comntained in the square
    Attributes:
        __size (int): one of the sides of the square
    """

    def __init__(self, size = 0):
        """intitializing the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        swlf.size = size

    def area(self):
        """Calculates the area ofr the square
        Returns:
            The area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of the __size
        Returns:
            size ofthe square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of the __size
        Args:
            value (int): the size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        else:
            if value <0:
                raise ValueError("Size must be greator or equal to 0")
            else:
                self.__size = value
