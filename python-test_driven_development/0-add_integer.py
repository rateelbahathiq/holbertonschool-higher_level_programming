#!/usr/bin/python3
"""Module for add_integer.
Adds two integers or floats.
Floats are cast to integers.
Validates input types first.
Returns an integer result.
"""


def add_integer(a, b=98):
    """Add two integers or floats as integers.
Floats are cast to integers before addition.
Return the integer sum of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
