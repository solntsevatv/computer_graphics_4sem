"""
    Digital differential analyzer algoritghm.
"""
from src.operations import my_round

def dda(x_start, y_start, x_end, y_end, color):
    """
        Implementation of DDA algorithm.
    """

    dx = x_end - x_start
    dy = y_end - y_start

    l = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    dx /= l
    dy /= l

    x = x_start
    y = y_start

    dots = []

    for _ in range(1, my_round(l) + 1):
        dots.extend([[my_round(x), my_round(y), color]])
        x += dx
        y += dy

    return dots
