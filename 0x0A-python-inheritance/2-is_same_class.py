#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class."""


def is_same_class(obj, a_class):
    """Check if obj is an instance of the class a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare obj to.
    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
