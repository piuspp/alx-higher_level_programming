#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """The class that create sqaure"""

    def __init__ (self, size=0):
        """
        create an instance

        Args:
            size(int):the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

            self.__size = size
    def area(self):
        """Returns square of current area

        Args:
            None
        
        Returns:
            Area of the square(int)
        """
        return(self.__size**2)


