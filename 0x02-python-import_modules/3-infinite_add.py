#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":

    # Use a generator expression to sum all integers from command-line arguments
    result = sum(int(arg) for arg in argv[1:])

    print(result)

