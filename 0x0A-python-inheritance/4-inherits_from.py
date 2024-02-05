#!/usr/bin/python3
#!/usr/bin/python3
"""A function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the specified class; otherwise False."""

def inherits_from(obj, a_class):
    """Function to check if obj is an instance of a class inherited from a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

