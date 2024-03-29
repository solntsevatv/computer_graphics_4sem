"""
    Bresenham algorithm.
"""

from src.operations import my_round


def bresenham_db(x_start, y_start, x_end, y_end, color):
    """
        Implementation of Bresenham float algorithm.
    """

    dx = my_round(x_end - x_start)
    dy = my_round(y_end - y_start)

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    m = dy / dx
    e = m - 0.5
    y = 0

    dots = []

    for x in range(dx + 1):
        dots.extend([[x_start + x*xx + y*yx, y_start + x*xy + y*yy, color]])
        if e >= 0:
            y += 1
            e -= 1
        e += m

    return dots

def bresenham_int(x_start, y_start, x_end, y_end, color):
    """
        Implementation of Bresenham integer algorithm.
    """

    dx = my_round(x_end - x_start)
    dy = my_round(y_end - y_start)

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    e = 2 * dy - dx
    y = 0

    dots = []

    for x in range(dx + 1):
        dots.extend([[x_start + x*xx + y*yx, y_start + x*xy + y*yy, color]])
        if e >= 0:
            y += 1
            e -= 2 * dx
        e += 2 * dy

    return dots

def bresenham_antialiased(x_start, y_start, x_end, y_end, color):
    """
        Implementation of Bresenham antialiased algorithm.
    """

    dx = x_end - x_start
    dy = y_end - y_start

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    m = dy / dx
    e = 0.5
    w = 1
    y = 0

    dots = []

    for x in range(round(dx + 1)):
        dots.extend([[x_start + x*xx + y*yx, y_start + x*xy + y*yy,
                      color + (255 * (1 - e), 255 * (1 - e), 255 * (1 - e))]])
        # dots.extend([[x_start + x*xx + y*yx + yx, y_start + x*xy + y*yy + yy,
        #               color + (255 * (1 - e), 255 * (1 - e), 255)]])
        if e >= w - m:
            y += 1
            e -= w
        e += m

    return dots
