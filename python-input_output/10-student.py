#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the instance.
        If attrs is a list of strings, return only those attributes.
        """
        if (isinstance(attrs, list) and
                all(type(attr) is str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
