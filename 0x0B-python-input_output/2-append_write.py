#!/usr/bin/python3
"""function to append a string at the end of the file"""

def append_write(filename="", text=""):
    """The attributes to be appended

    Args:
        filename: The name of file to be appended to 
        text: the string to be appended to the file
    Returns:
        Number of characters written
    """
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)
