#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "times", getattr(magic_string, "times", -1) + 1)
    return "BestSchool" + ", BestSchool" * getattr(magic_string, "times", 0)
