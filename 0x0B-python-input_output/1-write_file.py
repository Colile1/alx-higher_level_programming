#!/usr/bin/python3
"""Write the provided text to a UTF8 file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file.

    Args:
        filename (str): File name.
        text (str): Text to write.
    Returns:
        Characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
