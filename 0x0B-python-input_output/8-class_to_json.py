#!/usr/bin/python3
"""Return the dictionary representation of a simple data structure."""


def class_to_json(obj):
    """Return the dictionary representation of obj."""
    return(obj.__dict__)
