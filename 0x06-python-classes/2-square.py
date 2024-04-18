#!/usr/bin/python3
""" Class taht defines a sqaure cont.."""


class Square:
    """ Creates a class square"""

    def __init__ (self, size=0):
             """Initializes an instance"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
