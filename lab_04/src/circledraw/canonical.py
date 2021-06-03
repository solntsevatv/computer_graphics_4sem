"""
    Canonical equation.
"""

from math import sqrt
from src.circledraw import util


def cancircle(x_center, y_center, radius, color):
    """
        Implementation of circle canonical equation method.
    """

    dots = []

    for x in range(x_center, x_center + int(radius / sqrt(2)) + 1):
        y = sqrt(radius**2 - (x - x_center)**2) + y_center
        util.tmirrored(dots, x, y, x_center, y_center, color)

    return dots


def canellipse(x_center, y_center, a, b, color):
    """
        Implementation of ellipse canonical equation method.
    """

    dots = []
    limit = int(x_center + a / sqrt(1 + b**2 / a**2))

    for x in range(x_center, limit + 1):
        y = sqrt(a**2 * b**2 - (x - x_center)**2 * b**2) / a + y_center
        util.dmirrored(dots, x, y, x_center, y_center, color)

    limit = int(y_center + b / sqrt(1 + a**2 / b**2))

    for y in range(limit, y_center - 1, -1):
        x = sqrt(a**2 * b**2 - (y - y_center)**2 * a**2) / b + x_center
        util.dmirrored(dots, x, y, x_center, y_center, color)

    return dots
