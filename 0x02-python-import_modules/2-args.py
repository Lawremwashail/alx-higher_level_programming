#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_count = len(sys.argv) - 1
    if num_count == 0:
        print("0 args")
    elif num_count == 1:
        print("1 arg")
    else:
        print("{} args:".format(count))
    for i in range(num_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
