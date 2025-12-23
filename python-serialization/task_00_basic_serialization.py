#!/usr/bin/python3
"""Basic serialization and deserialization module."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON
    and save it into a file.
    Replaces the file if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and
    deserialize it back into a Python dictionary.
    Returns the dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
