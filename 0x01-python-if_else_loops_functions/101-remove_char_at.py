#!/usr/bin/python3

def remove_char_at(str, n):
    new_char = ''
    i = 0
    for char in str:
        if i != n:
            new_char += str[0]
        i++
    return (new_char)
