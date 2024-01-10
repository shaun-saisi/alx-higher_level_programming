#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_unique = 0
    seen_numbers = set()

    for num in my_list:
        if num not in seen_numbers:
            sum_unique += num
            seen_numbers.add(num)

    return sum_unique
