#!/usr/bin/python3

class Square:
    """ This is a square with a private instance attribute which is size"""

    def __init__(self, size = 0):
        """
         Args:
            size: This is thes izeof tthe square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("Size must be greator than zero")
            else:
                self.__size = size
        else:
            :raise TypeError('Size must be an integer')
