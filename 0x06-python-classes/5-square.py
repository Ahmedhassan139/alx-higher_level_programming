#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """optional initialization with size=0 which a positive int"""

    def __init__(self, size=0):
        """initilializes with size 0"""
        self.__size = size

    @property
    def size(self):
        """method to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method that returns area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """method that prints a square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * "#")
              
