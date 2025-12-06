#!/usr/bin/python3
"""
Module that defines text_indentation function.
Splits text on ., ? and : then prints with new lines.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text: input string

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            print(result.strip())
            print()  # prints two new lines total
            result = ""

    if result.strip() != "":
        print(result.strip())
