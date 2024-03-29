#!/usr/bin/python3
"""A class square that inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """The inherited class"""
    def __init__(self, size):
        """The size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of the square"""
        return self.__size ** 2
    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
