#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This is my first class."""

    def __init__(self, size=0):
        """
        Initialize an instance of the Square class with a private attribute.
        """
        self.__size = size  # Private attribute
        if not isinstance(size, int):
            raise TypeError("size is not an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
