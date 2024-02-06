#!/usr/bin/python3
"""Function returns dictionary description of dat"""

def class_to_json(obj):
    """the object to contain the data"""
    return obj.__dict__
