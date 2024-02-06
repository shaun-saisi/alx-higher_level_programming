#!/usr/bin/python3
"""Function returns an obj from a json string"""

import json

def from_json_string(my_str):
    """The string to be loaded"""
    return json.loads(my_str)
