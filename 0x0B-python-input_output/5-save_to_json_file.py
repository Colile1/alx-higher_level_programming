#!/usr/bin/python3
"""Write object to file using JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to file as JSON."""
    with open(filename, "w") as f:
        return(json.dump(my_obj, f))
