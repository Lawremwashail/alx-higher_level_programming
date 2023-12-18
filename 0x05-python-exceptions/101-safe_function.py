#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
        return output
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
