#!/usr/bin/python3
"""
A module to add two numbers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Performs the addition between two numbers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
