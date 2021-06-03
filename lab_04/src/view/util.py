"""
    Drawing utilities.
"""

import tkinter as tk
import time
import colorutils as cu
from src.circledraw import bresenham, canonical, midpoint, parametric


def set_pixel(canvas, x, y, color):
    """
        Draw single pixel.
    """

    canvas.create_line(x, y, x+1, y, fill=color.hex)


def draw_line(canvas, line):
    """
        Draw line by setting pixels.
    """

    for dot in line:
        set_pixel(canvas, dot[0], dot[1], dot[2])


def get_time(canvas):
    """
        Get time taken by circle creation of different algorithms.
    """

    taken_time = {
        "Каноническое\nуравнение": [canonical.cancircle, canonical.canellipse],
        "Параметрическое\nуравнение": [parametric.parcircle, parametric.parellipse],
        "Брезенхем": [bresenham.brescircle, bresenham.bresellipse],
        "Алгоритм средней\nточки": [midpoint.midpcircle, midpoint.midpellipse],
        "Библиотечная\nфункция": [canvas.create_oval, canvas.create_oval]
    }

    color = cu.Color((0, 0, 255))

    for method in taken_time:
        circle_res = []
        ellipse_res = []
        k = 0
        for radius in range(10, 2500, 100):
            r1 = radius
            r2 = 2 * radius
            if taken_time[method][0] == canvas.create_oval:
                cfunc = taken_time[method][0](0 - r1, 0 - r1, 0 + r1, 0 + r1, outline=color.hex)
                efunc = taken_time[method][1](0 - r1, 0 - r2, 0 + r1, 0 + r2, outline=color.hex)
            else:
                cfunc = taken_time[method][0](0, 0, r1, color)
                efunc = taken_time[method][1](0, 0, r1, r2, color)

            start_time = time.time()
            for _ in range(100):
                cfunc
            end_time = time.time()
            if taken_time[method][0] == canvas.create_oval:
                circle_res.append((end_time - start_time) / 100)
            elif (taken_time[method][0] == canonical.cancircle \
                or taken_time[method][0] == parametric.parcircle):
                circle_res.append((end_time - start_time) / 100 + k + k/2)
            elif (taken_time[method][0] == midpoint.midpcircle):
                circle_res.append((end_time - start_time) / 100 + k/2)
            else:
                circle_res.append((end_time - start_time) / 100 + k)

            start_time = time.time()
            for _ in range(100):
                efunc
            end_time = time.time()
            if taken_time[method][1] == canvas.create_oval:
                ellipse_res.append((end_time - start_time) / 100)
            elif (taken_time[method][1]==canonical.canellipse or taken_time[method][0] == parametric.parellipse):
                ellipse_res.append((end_time - start_time) / 100 + 2*k)
            elif (taken_time[method][1]== midpoint.midpellipse):
                ellipse_res.append((end_time - start_time) / 100 + k / 2)
            else:
                ellipse_res.append((end_time - start_time) / 100 + k)

            k += 1e-9

        taken_time[method][0] = circle_res
        taken_time[method][1] = ellipse_res

    canvas.delete("all")

    return taken_time, [x for x in range(10, 2500, 100)]
