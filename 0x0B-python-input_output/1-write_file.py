#!/usr/bin/python3
"""Function that writes to astring"""

def write_file(filename="", text=""):
    """writes a file and encodes it

    Args:
        filename: The name of the file to write
        text: the text to be written to the file
    Returns:
        The number of characters written
        """

    with open(filename, "w", encoding="UTF8") as file:
        content = file.write(text)
        print(content)
