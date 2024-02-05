#!/usr/bin/python3
""" A class MYLIst that inherits fromm list"""

class MyList(list):
    """ Class my list prints out lists sorted in ascending
    Args: print_sorted: function that sorts the list
    """
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print (sorted(self))
