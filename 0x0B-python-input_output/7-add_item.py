#!/usr/bin/python3
"""Add the arguments in a python list"""
import sys
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Extend items with command-line arguments
    items.extend(sys.argv[1:])

    # Save the updated items to the JSON file
    save_to_json_file(items, "add_item.json")

