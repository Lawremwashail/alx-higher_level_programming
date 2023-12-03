#!/usr/bin/python3i
def no_c(my_string):

    my_new_string = ""

    for character in my_string:
        if character.lower() != 'c':
            my_new_string += character
        return my_new_string
