#!/usr/bin/python3
"""
la on commence les test unitaire en python, on met la fonction ici
"""


def matrix_divided(a[], int b):
    """
    Adds two integers or floats after casting them to integers.
    Args:
        a: c'est un tableau mais il lui faut plusieurs dimensions
        b: c'est le diviseur, il divise tout les elemen du tableau
    Returns:
        The addition of a and b as an integer.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (array)):
        raise TypeError("matrix must be a matrix")
    if 
    if not isinstance(b, (int)):
        raise TypeError("div must be a number")

    # Cast to integer before adding
    return int(a) + int(b)
