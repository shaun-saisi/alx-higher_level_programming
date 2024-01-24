#!/usr/bin/python3
"""it defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        Args:
            size: the size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be equal or greator than 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
