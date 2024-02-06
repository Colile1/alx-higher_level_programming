#!/usr/bin/python3
"""Print the contents of a UTF8 text file."""


def read_file(filename=""):
    """Print UTF8 file contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
