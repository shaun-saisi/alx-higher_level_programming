#!/usr/bin/python3
"""function that writes a n object file to a text file using json format"""

import json

def save_to_json_file(my_obj, filename):
    """the objects and filename to be written to
    
    Args:
        my_obj: the object to be written
        filename: filename to receive the object
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
