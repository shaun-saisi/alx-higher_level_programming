#!/usr/bin/python3
import os
def list_hidden_files(directory='hidden_4.pyc'):
    # Get a list of all files in the directory
    all_files = os.listdir(directory)

    # Filter out hidden files (those starting with '.')
    hidden_files = [file for file in all_files if not file.startswith('.')]

    # Sort the list alphabetically
    hidden_files.sort()

    # Print one name per line
    for file in hidden_files:
        print(file)

# Run the function if the script is executed
if __name__ == "__main__":
    list_hidden_files()
