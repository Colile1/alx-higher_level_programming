#!/usr/bin/python3
"""Return Python object representation of a JSON string."""  
import json


def from_json_string(my_str):
    """Return Python object for JSON string."""
    return(json.loads(my_str))
