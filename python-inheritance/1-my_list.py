#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print sorted elements."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        new_list = self[:]
        new_list.sort()
        print(new_list)
