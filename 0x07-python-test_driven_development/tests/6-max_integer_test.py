#!/usr/bin/python3
"""
A function that adds two integers
"""

def add_integer(a, b=98):
    """
    A function that adds two integers, converts floats to integers

    Args:
        a: first integer
        b: second integer

    Returns:
        The sum of the two given numbers

    Raises:
        TypeError: If a or b are not either integer or float numbers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
