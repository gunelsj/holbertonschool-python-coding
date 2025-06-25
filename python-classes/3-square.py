#!/usr/bin/python3
"""Square class that defines a square by its size with getter and setter."""


class Square:
    """A class that defines a square by its size."""
    
    def __init__(self, size=0):
        self.size = size  # Automatically calls the setter

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
