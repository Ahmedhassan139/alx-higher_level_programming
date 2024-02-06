#!/usr/bin/python3
"""program that creates the class Square that defines a square"""


class Square:
    """defines a square by its size"""

    def __init__(self, size=0):
        """optional initialization with private attribute size, an int >= 0"""
        self._size = size

    @property
    def size(self):
        """method to retrieve size value"""
        return size

    @size.setter
    def size(self, value):
        """method to set size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """returns area of the square"""
        return (self._size**2)
      
