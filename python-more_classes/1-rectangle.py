#!/usr/bin/python3
"""Define class rectangle."""


class Rectangle:
    """Add Private instance attributes: width and height."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width and validate it."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height and validate it."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value   
