#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)."""
    if my_list is None:
        return 0
    return sum(set(my_list))
