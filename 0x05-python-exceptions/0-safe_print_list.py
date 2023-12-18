#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        value = 0
        for i in range(x):
            print(my_list[i], end="")
            value += 1
    except IndexError:
        break
    print()
    return (value)
