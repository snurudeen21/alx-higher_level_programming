#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, mode="a", encoding="utf-8") as fm:
        fm.write(text)
    return len(text)
