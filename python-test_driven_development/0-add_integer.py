#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Return the sum of two integers or floats after casting floats to ints.

    Args:
        a: first number
        b: second number, default = 98

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
