#!/usr/bin/python3

""" The class square below has a private instance attribute size
which is instantiated"""

class Square:
    """Represents a square with attributes"""
    def __init__(self, size):
        """Initializes a square
        Args: size(int) : side of the square size
        Returns:Nothing"""
        self.__size = size
