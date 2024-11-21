#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This is my first class."""

    def __init__(self, size=0):
        """
        Initialize an instance of the Square class with a private attribute.
        """
        self.__size = size  # Private attribute
        assert isinstance(size, int), "size is not an integer"
