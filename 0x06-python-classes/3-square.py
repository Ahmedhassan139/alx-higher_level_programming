#!/usr/bin/python3
"""program that creates a class Square which defines a square"""


class Square:
    """private attribute is size"""

    def __init__(self, size=0):
        """optional init, size must be a positive integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        """returns current square area"""
        return (self._size**2)
      
