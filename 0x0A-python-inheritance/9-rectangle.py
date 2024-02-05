#!/usr/bin/python3
"""
Contains parentclass BaseClass and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class rectangle with instantiation attributes"""
    def __init__(self, width, height):
        """Initialization of the rectangle
        Args:
            width- the width of the rectangle
            height - the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """Magic method to return representation of a rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
