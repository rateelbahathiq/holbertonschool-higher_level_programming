#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Return a set of common elements in two sets."""
    if set_1 is None or set_2 is None:
        return set()
    return set_1 & set_2
