#!/usr/bin/python3
"""Create Python object from JSON file."""  
import json


def load_from_json_file(filename):
    """Load Python object from JSON file."""
    with open(filename) as f:
        return(json.load(f))
