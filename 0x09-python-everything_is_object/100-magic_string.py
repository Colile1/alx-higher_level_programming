#!/usr/bin/python3
def magic_string():
    """
    This function increments the value of 'n' for each call and returns a string with the pattern "BestSchool, " repeated 'n' times, followed by "BestSchool".
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
