#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def width(self, width):
        self.width = width
        
        @property
        def width(self):
            return self.width

        @width.setter
        def width (self, width):
            if isinstance(width):
                raise TypeError 
                print("width must be an integer")
            elif width < 0:
                raise ValueError
                print("width must be >= 0")

     def height(self, height):
        self.height = height
        
        @property
        def height(self):
            return self.height
        
        @height.setter
        def height(self, height):
            if isinstance(height):
                raise TypeError 
                print("height must be an integer")
            elif height < 0:
                raise ValueError
                print("height must be >= 0")

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
