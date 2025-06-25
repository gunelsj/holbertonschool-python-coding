#!/usr/bin/python3
"""Square class that defines a square by its size with getter and setter."""


class Square:
    """A class that defines a square by its size."""
    
    def __init__(self, size=0):
        self.size = size  # Automatically calls the setter
