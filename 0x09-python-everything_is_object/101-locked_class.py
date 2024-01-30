#!/usr/bin/python3
""" This is a locked class"""


class LockedClass:
    """ Prevents instantiation of a locked class
    just the first_ name allowed
    """

    __slots__ = ["first_name"]
