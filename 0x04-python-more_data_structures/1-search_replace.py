#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = list(map(lambda n: replace if n == search else n, mylist))
    return (my_new_list)
