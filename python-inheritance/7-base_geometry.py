#!/usr/bin/python3
"""
Defines a BaseGeometry class with area and integer validation methods.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer greater than 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
