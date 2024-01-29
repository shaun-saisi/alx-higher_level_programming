#!/usr/bin/python3

class Rectangle:
    """
    Basic definition of a rectangle with its properties

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle object

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width of the rectangle.

        Args:
            value (int): Width value to be set
        Raises:
            TypeError: If width is not an integer
            ValueError: If the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height of the rectangle.

        Args:
            value (int): Height value to be set
        Raises:
            TypeError: If height is not an integer
            ValueError: If the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

