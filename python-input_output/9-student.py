#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the instance."""
        return self.__dict__
