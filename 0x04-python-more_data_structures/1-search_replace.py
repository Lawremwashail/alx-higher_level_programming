#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = list(map(lambda e: replace if e == search else e, mylist))
    return my_new_list
