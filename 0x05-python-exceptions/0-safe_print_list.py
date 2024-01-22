#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print(my_list[i], end = ' ')
            count += 1
    except IndexError:
        print("This is an index errror")
    finally:
        print()
    return count
