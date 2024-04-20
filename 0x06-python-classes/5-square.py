#!/usr/bin/python3
"""The square module continue"""


class Square:
    """The class to create square."""

    def __init__(self, size=0):
        """set size to private instance

        Args:
            size(int):size of new square
        """
        self.__size = size

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
        """getter that get size variable"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set thesize to the value

        Args:
            value: the value to reset
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to that returns the area based on the size"""
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
