#!/usr/bin/python3
def no_c(my_string):
    filter_chars = [char for char in my_string if char not in ('c', 'C')]
    new_string = ''.join(filter_chars)
    return new_string
