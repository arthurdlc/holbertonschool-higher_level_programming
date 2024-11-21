#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This is my first class."""

    def __init__(self, size=0):
        """
        Initialize an instance of the Square class with a private attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Equivalent d'un this en java/php

    def area(self):
        """
        c'est une methode qui renvoie l'air de l'objet en faisant size²
        """
        return self.__size ** 2
