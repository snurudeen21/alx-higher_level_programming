#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num = len(sys.argv)

    if num == 1:

        print(f"{num - 1} arguments.")

    elif num == 2:

        print(f"{num - 1} argument:")

    else:

        print(f"{num - 1} arguments:")

    for i in range(1, num):

        print(f"{i}: {sys.argv[i]}")
