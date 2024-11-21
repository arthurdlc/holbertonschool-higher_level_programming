#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square.

        Args:
            size (int): The size of the square's sides (default is 0).
            position (tuple): The position offset (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the `#` character.

        The square is offset by `position`. If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
