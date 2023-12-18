#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        output = a / b
    except (ZeroDivisionError, TypeError):
        return None
    finally:
        print("Inside result: {}".format(output))
        return output
