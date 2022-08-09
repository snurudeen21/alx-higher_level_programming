#!/usr/bin/python3

""" Calculate area of Square """


def square_area(length):
    if length < 0:
        raise ValueError("Please enter a positive integer")
    return length**2
