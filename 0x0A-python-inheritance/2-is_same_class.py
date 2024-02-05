#!/usr/bin/python3
""" Function that returns an instance of a specific class"""

def is_same_class(obj, a_class):
    """ function to checkk whether the object is same
    Args:
        obj- the object to be checked
        a_class - the second object to be compared
    """
    return (type(obj) == a_class)
