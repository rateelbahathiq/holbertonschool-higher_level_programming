#!/usr/bin/python3
"""Module that converts a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)."""
    return json.dumps(my_obj)
