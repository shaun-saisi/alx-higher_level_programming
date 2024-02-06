#!/usr/bin/python3
"""function that returns a list of integers"""

def pascal_triangle(n):
    """the function containing the list of ints"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tr = triangle[-1]
        tmp = [1]
        for i in range(len(tr) -1):
            tmp.append(tr[i] + tr[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
