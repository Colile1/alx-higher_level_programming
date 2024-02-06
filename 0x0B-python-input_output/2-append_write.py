#!/usr/bin/python3
"""Appends text to a UTF8 file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): File to append to
        text (str): text(str): String to append.
    Returns:
        Num chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
