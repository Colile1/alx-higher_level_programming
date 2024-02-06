#!/usr/bin/python3
"""defines a class myint that inherits from int."""


class myint(int):
    """invert int operators == and !=."""

    def __eq__(self, value):
        """override == opeartor with != behavior."""
        return (self.real != value)

    def __ne__(self, value):
        """override != operator with == behavior."""
        return (self.real == value)
