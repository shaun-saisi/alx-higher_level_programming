#!/usr/bin/python3
"""function to read a text file"""

def read_file(filename=""):
    """prints the content of the file"""
    with open('example.txt', 'r', encoding="utf-8") as file:
        print(f.read(), end =""
