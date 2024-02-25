#!/usr/bin/python3
"""
A function that prints text with two new lines after each '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    Returns:
        Nothing.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i)
            print()
        else:
            print(i, end="")
