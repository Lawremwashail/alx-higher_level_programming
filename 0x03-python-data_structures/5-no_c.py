#!/usr/bin/python3i
def no_c(my_string):
    my_new_string = ""
    for character in range(len(my_string)):
        if (my_string[character] != 'c' and my_string[character] != 'C'):
            my_new_string += my_string[character]
    return my_new_string
