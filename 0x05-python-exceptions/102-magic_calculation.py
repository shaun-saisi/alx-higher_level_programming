#!/usr/bin/python3
def magic_calculation(a, b):
    rslt = 0

    for  in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            rslt += a ** b / i
        except:
            rslt = b + a
            break

    return rslt
