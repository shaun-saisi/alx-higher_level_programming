#!/usr/bin/python3

"""Function returns the list of attreibutes"""

def lookup(obj):
    """
        Lookup function that returns a list of attributes and methods
    Args: obj- The objects to be returned
    Return: A list of objects
    """
    return dir(obj)
