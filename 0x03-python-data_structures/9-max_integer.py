#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_number = my_list[0]
    else:
        for number in my_list[1:]:
            if number > max_number:
                max_number = number
        return max_number
