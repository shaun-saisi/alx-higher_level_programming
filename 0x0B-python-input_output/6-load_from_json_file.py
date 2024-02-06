#!/usr/bin/python3
"""function creates an object from a json file"""

import json

def load_from_json_file(filename):
    """filename to load the object"""
    with open(filename, 'r') as file:
        return json.load(file)
