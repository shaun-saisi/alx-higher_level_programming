#!/usr/bin/python3

"""Function returns JSON format of an object string"""
import json

def to_json_string(my_obj):
    """the object to return a json rep"""
    json_my_obj = json.dumps(my_obj)
    return json_my_obj
