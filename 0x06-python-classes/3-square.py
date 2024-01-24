#!/usr/bin/python3
""" the class defines a square """

class Square:
    """ a square with a private instance attribute known as size"""

    def __init__(self, size=0):
        """
        Initializes the square
        Args:
            size: the size of the squre which has all siz=des equal
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be greator or equal to 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds the area of the square based on the size
        Reurns:
            the area
        """

        return self.__size ** 2
