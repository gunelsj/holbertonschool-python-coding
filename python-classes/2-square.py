#!/usr/bin/python3
"""Square class defines a square by size and calculates area"""


class Square:
    """Class to define a square"""

    def __init__(self, size=0):
        """Initialize the square with optional size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return area of square"""
        return self.__size ** 2
