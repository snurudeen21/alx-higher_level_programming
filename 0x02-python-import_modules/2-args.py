#!/usr/bin/python3

if _name_ == "_main_":
    from sys import argv
    length = len(argv)

    if length == 1:
        print(f"{length - 1:d} arguments.")
    elif length == 2:
        print(f"{length - 1:d} argument:")
        print(f"1: {argv[length - 1]:s}")
    else:
        print(f"{length - 1:d} arguments:")
        for i in range(1, length):
            print(f"{i}: {argv[i]:s}")
