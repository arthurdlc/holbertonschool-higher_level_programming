#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square with size and calculates its area."""

    def __init__(self, size: int = 0):
        """
        Initialize an instance of the Square class.

        Args:
            size (int): The size of the square's sides. Must be >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self) -> int:
        """int: Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the `#` character.

        If the size of the square is 0, print a blank line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
