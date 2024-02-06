#!/usr/bin/python3
"""Return JSON representation of a string object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string."""
    return([json.dumps(my_obj)])
