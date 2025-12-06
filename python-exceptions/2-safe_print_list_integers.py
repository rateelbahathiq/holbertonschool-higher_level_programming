#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements that are integers."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except Exception:
            pass
    print()
    return count
