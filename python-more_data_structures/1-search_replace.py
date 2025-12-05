#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Return a new list with all occurrences of search replaced."""
    if my_list is None:
        return None
    return [replace if x == search else x for x in my_list]
