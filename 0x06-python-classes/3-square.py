#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """The class to create square."""

    def __init__(self, size=0):
        """set size to private instance variable

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """get the area of the square

        Args:
            None

        Returns:
            Area of the square(int)
        """
        return (self.__size * self.__size)
