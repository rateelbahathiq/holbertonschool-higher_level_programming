#!/usr/bin/python3
"""Module that defines the read_file function.
Reads a text file (UTF8) and prints its contents to stdout.
"""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
