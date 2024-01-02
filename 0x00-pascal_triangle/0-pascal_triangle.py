"""Pascal's Triangle"""
from math import factorial as f


def short_triangle(ui):
    """
    ui: integer
    Returns: list of integers
    representing the Pascal's triangle
    """
    return [f(ui) // (f(i) * f(ui - i)) for i in range(ui + 1)]


def pascal_triangle(n):
    """
    n: integer
    Return: list of lists of integers
    representing the Pascal's triangle
    """
    if n <= 0:
        return []

    return [short_triangle(i) for i in range(0, n)]
