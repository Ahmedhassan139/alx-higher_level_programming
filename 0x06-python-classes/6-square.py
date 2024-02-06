#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """optional initialization with size=0 which a positive int"""

    def __init__(self, size=0, position=(0,0)):
        """initilializes with size 0 and position at (0,0)"""
        self._size = size
        self._position = position

    @property
    def size(self):
        """method to retrieve size"""
        return size

    @size.setter
    def size(self, value):
        """method to set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @position
    def position(self):
        """method that returns position"""
        return position

    @position.setter
    def position(self, value):
        """method to set position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def area(self):
        """method that returns area of the square"""
        return (self._size**2)

    def my_print(self):
        """method that prints a square"""
        if size is 0:
            print()
        for i in range(value[0], value[0] + size):
            for j in range(value[1], value[1] + size):
                print("#", end="")
            print()
          
