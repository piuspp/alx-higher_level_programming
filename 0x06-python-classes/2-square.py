#!/usr/bin/python3
""" Class taht defines a sqaure cont.."""


class Square:
    """ Creates a class square"""

    def __init__ (self, size=0):
             """set size to private instance variable

        Args:
            size (int): the size of the square
        """

        if int(size) != size:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
