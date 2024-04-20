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

    def area(self):
        """get the area of the square

        Args:
            None

        Returns:
            Area of the square(int)
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns the size of the sqaure"""
        return (self.size)
    
    @size.setter
    def size(self, value):
        """
            Asigns value to size

        Args:
            value: the value of the set size
        """

        if not isinstance(value, int):
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")
        self._size = value


