#!/usr/bin/python3
"""Defines a function that returns Pascal's Triangle of a given size."""


def pascal_triangle(n):
    """Return a list of lists of ints representing Pascal's Triangle of size n.
    
    The triangle has rows representing the current row number. Each row has number 
    of ints equal to the row number. The first and last int in every row is 1, with
    the rest of the ints calculated by adding the 2 ints above in the triangle.
    """
    if(n <= 0):
        return([])

    triangles = [[1]]
    while(len(triangles) != n):
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return(triangles)
