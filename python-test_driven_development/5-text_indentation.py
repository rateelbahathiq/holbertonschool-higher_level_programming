#!/usr/bin/python3
"""
Module that defines text_indentation function.
Splits text on '.', '?' and ':' and prints it.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text: input text (must be a string)

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for char in text:
        # Skip leading spaces at the beginning of a new block/line
        if not new_line and char == " ":
            continue
        else:
            new_line = True

        if char in ".?:":
            print(char)
            print()     # blank line => total 2 newlines
            new_line = False
        else:
            print(char, end="")

    # Ensure final printed line ends with a newline
    if new_line:
        print()
