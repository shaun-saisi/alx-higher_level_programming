#!/usr/bin/python3
"""a class rectangle with area and perimeter"""


class Rectangle:
    """Just a rectangle"""
    def __init__(self, width =0, height=0):
        """Initializing the rectangle"""
        self.width = self
        self.height = self

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an ingteger")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be int")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__ = value
    def perimeter(self):
        """The perimether of the rect"""
        if self.___width == 0 or self.__height = 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def area(self):
        """the area of the rectangle"""
        return self.__height * self.__width
