#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result."""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
