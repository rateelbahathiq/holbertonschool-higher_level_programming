#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text: input text (string)

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            # print the current sentence, stripped, followed by a blank line
            print(buffer.strip())
            print()
            buffer = ""

    # Print remaining text (if any) WITHOUT extra newline at the end
    remaining = buffer.strip()
    if remaining != "":
        print(remaining, end="")
