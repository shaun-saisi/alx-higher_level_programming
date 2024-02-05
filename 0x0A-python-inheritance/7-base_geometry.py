#!/usr/bin/python3
""" A class containing BaseGeometry"""

class BaseGeometry:
    """The class containing methods"""
    def area(self):
        """The area method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """method validates the value"""
        if type(value) is not int:
            raise ValueError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
