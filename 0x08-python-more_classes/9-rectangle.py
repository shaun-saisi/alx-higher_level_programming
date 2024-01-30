#!/usr/bin/python3
"""Class Rectangle with area and perimeter"""


class Rectangle:
    """Just a rectangle"""
    number_of_instances = 0
    print_symbol = "#"  # Added correct indentation for the class variables

    def __init__(self, width=0, height=0):
        """Initializing the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __del__(self):
        """Print a delete message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def perimeter(self):
        """The perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def area(self):
        """The area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Returns a string"""
        string = ""
        if self.__height != 0 and self.__width != 0:
            string += "\n".join("#" * self.__width for _ in range(self.__height))
        return string

    def __repr__(self):
        """Returns a representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
