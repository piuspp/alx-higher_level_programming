#!/usr/bin/python3
""" Class that defines a square"""


class Square:
    """This creates the class square"""

    def __init__ (self, size=0):
        """
            Creates a private instance 

        Args:
            size(int): the size of a square
        """

        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        self._size = size

    def set_size():

