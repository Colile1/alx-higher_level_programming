#!/usr/bin/python3
"""Check if object is instance or subclass of a class."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance/subclass of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match type of obj.
    Returns:
        If obj is instance/subclass of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
