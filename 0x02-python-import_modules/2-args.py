#!/usr/bin/python3
from sys import argv

number_of_arguments = len(argv) - 1 # Minus 1 is used to exclude the script name

print(f"{number_of_arguments} argument{'s' if number_of_arguments > 1 else ' '}:")
for i, arg in enumerate(argv[1:], start=1):
    print(f"{i}: {arg}")
