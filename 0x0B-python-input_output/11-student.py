#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, only attributes named in the list
        are included. Otherwise, all attributes are included.
        """
        if attrs is None:
            return self.__dict__
        return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        
        Assume json will always be a dictionary with keys for the attribute 
        names and values for the corresponding values.
        """
        for key, value in json.items():
            setattr(self, key, value)
