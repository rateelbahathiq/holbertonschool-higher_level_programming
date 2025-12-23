#!/usr/bin/python3
"""Module that defines the Student class with JSON support."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the instance.
        If attrs is a list of strings, return only those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
