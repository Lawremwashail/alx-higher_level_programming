#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    value = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            value += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
        return value
