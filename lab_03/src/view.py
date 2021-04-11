from src.const import *
import src.dda, src.bresenham, src.wu
from tkinter import messagebox
import colorutils as cu
from math import sin, radians, cos
import matplotlib.pyplot as plt
import timeit
import numpy as np
import time
import math

def ind_to_color(ind):
    if ind == 0:
        return GREY
    if ind == 1:
        return RED
    if ind == 2:
        return YELLOW
    if ind == 3:
        return GREEN
    if ind == 4:
        return BLUE
    if ind == 5:
        return BLACK
    if ind == 6:
        return WHITE

def translate_color(color):
    if color == GREY:
        return cu.Color((128, 128, 128))
    elif color == RED:
        return cu.Color((255, 0, 0))
    elif color == YELLOW:
        return cu.Color((255, 255, 0))
    elif color == GREEN:
        return cu.Color((0, 128, 0))
    elif color == BLUE:
        return cu.Color((0, 0, 255))
    elif color == BLACK:
        return cu.Color((0, 0, 0))
    elif color == WHITE:
        return cu.Color((255, 255, 255))

def name_to_func(root, method):
    func = root.canv.create_line
    if method == DDA:
        func = src.dda.dda
    elif method == "Брезенхем\n(целочисл.)" or method == BR_INT:
        func = src.bresenham.bresenham_int
    elif method == "Брезенхем\n(действит.)" or method == BR_FLOAT:
        func = src.bresenham.bresenham_db
    elif method == "Брезенхем\n(сглаживание)" or method == BR_ANTIALIASED:
        func = src.bresenham.bresenham_antialiased
    elif method == WU:
        func = src.wu.wu
    elif method == "Библиотечная\nфункция" or method == LIB_FUNC:
        func = root.canv.create_line
    return func

def draw(root):
    """
        Draw lines using different algorithms.
    """

    method = root.combo_box.get()
    color = ind_to_color(root.v_pen.get())
    color_cu = translate_color(color)

    dots = None
    x_start, x_end, y_start, y_end = None, None, None, None

    try:
        x_start = float(root.entry_x_start.get())
        y_start = float(root.entry_y_start.get())
        x_end = float(root.entry_x_end.get())
        y_end = float(root.entry_y_end.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Неккоретное число.")

    if abs(x_start - x_end) < 1e-6 and abs(y_end - y_start) < 1e-6:
        set_pixel(root.canv, x_start, y_start, color_cu)
        method = LIB_FUNC
    elif method == DDA:
        dots = src.dda.dda(x_start, y_start, x_end, y_end, color_cu)
    elif method == BR_INT:
        dots = src.bresenham.bresenham_int(x_start, y_start, x_end, y_end, color_cu)
    elif method == BR_FLOAT:
        dots = src.bresenham.bresenham_db(x_start, y_start, x_end, y_end, color_cu)
    elif method == BR_ANTIALIASED:
        dots = src.bresenham.bresenham_antialiased(x_start, y_start, x_end, y_end, color_cu)
    elif method == WU:
        dots = src.wu.wu(x_start, y_start, x_end, y_end, color_cu)
    elif method == LIB_FUNC:
        root.canv.create_line(x_start, y_start, x_end, y_end, fill=color)

    if method != LIB_FUNC:
        draw_line(root.canv, dots)


def set_pixel(canvas, x, y, color):
    """
        Draw single pixel.
    """
    canvas.create_line(x, y, x+1, y+1, fill=color.hex)


def draw_line(canvas, line):
    """
        Draw line by setting pixels.
    """

    for dot in line:
        set_pixel(canvas, dot[0], dot[1], dot[2])

def change_canv_bg(root, color):
    root.canv.configure(bg = color)

def clean_canvas(root):
    root.canv.delete("all")
    root.canv.configure(bg = ind_to_color(root.v_bg.get()))

def draw_bunch(root):
    try:
        radius = int(root.entry_line_len.get())
        step = int(root.entry_angle.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Некорректное число.")
        return

    #clean_canvas(root.canv)

    color = ind_to_color(root.v_pen.get())
    color_cu = translate_color(color)
    method = root.combo_box.get()

    lines = 360 // step

    x_start = CANV_X // 2
    y_start = CANV_Y // 2 - radius
    x_end = CANV_X // 2
    y_end = CANV_Y // 2

    x_rotate = CANV_X // 2
    y_rotate = CANV_Y // 2

    dots = [(x_start, y_start, x_end, y_end)]
    fixed_step = step

    func = name_to_func(root, method)

    for _ in range(1, lines):
        x_s = x_rotate + (y_start - y_rotate) * sin(radians(step))
        x_e = x_rotate + (y_end - y_rotate) * sin(radians(step))
        y_s = y_rotate + (y_start - y_rotate) * cos(radians(step))
        y_e = y_rotate + (y_end - y_rotate) * cos(radians(step))
        step += fixed_step

        dots.append((int(x_s), int(y_s), int(x_e), int(y_e)))

    for pair in dots:
        if func == root.canv.create_line:
            func(pair[0], pair[1], pair[2], pair[3], fill=color)
        else:
            ds = func(pair[0], pair[1], pair[2], pair[3], color_cu)            
            draw_line(root.canv, ds)


def get_time(root, times):
    """
        Get time taken by line creation of different algorithms.
    """

    taken_time = {
        DDA: src.dda.dda,
        "Брезенхем\n(целочисл.)": src.bresenham.bresenham_int,
        "Брезенхем\n(действит.)": src.bresenham.bresenham_db,
        "Брезенхем\n(сглаживание)": src.bresenham.bresenham_antialiased,
        WU: src.wu.wu,
        "Библиотечная\nфункция": root.canv.create_line
    }

    color = cu.Color((0, 0, 255))

    for method in taken_time:
        curr1 = time.time()
        if taken_time[method] == root.canv.create_line:
            for i in range(50):
                taken_time[method](0.01, 0.01, 500, 500, fill=color.hex)
        else:
            for i in range(50):
                taken_time[method](0.01, 0.01, 500, 500, color)
        curr2 = time.time()
        times[method] = (curr2 - curr1) / 50

    clean_canvas(root)

    return times

def compare_algorithms(root):
    """
        Show diagram with time measurements.
    """
    times = {
        DDA: 0,
        "Брезенхем\n(целочисл.)": 0,
        "Брезенхем\n(действит.)": 0,
        "Брезенхем\n(сглаживание)": 0,
        WU: 0,
        "Библиотечная\nфункция": 0
    }

    get_time(root, times)

    times["Брезенхем\n(целочисл.)"], times["Брезенхем\n(действит.)"] = times["Брезенхем\n(действит.)"], times["Брезенхем\n(целочисл.)"]

    plt.figure(2, figsize=(9, 7))
    plt.bar(list(times.keys()), list(times.values()), align='center')
    plt.ylabel("Work time in sec. (line len. 100)")
    plt.show()
    

def turn_point(angle, p, center):
    x = p[0]
    p[0] = round(center[0] + (x - center[0]) * cos(angle) + (p[1] - center[1]) * sin(angle))
    p[1] = round(center[1] - (x - center[0]) * sin(angle) + (p[1] - center[1]) * cos(angle))

def calcStairsCount(segLength, angle):
    deg_to_rad = math.pi / 180

    if (angle > 45):
        angle = 90 - angle
    
    return round(segLength * sin(angle * deg_to_rad))

# Анализ ступечатости
def smoth_analyze(root):
    try:
        length = int(root.entry_line_len.get())
    except ValueError:
        length = 100


    angles = [i for i in range(5, 91, 5)]
    dda = []
    br_int = []
    br_float = []
    br_antial = []
    wu = []
    names = [dda, br_int, br_float, br_antial, wu]
    LENGTH = 345

    center = [CANV_X // 2, CANV_Y // 2]

    for i in names:
        for j in angles:
            i.append(calcStairsCount(LENGTH, j))
            
    fig, ax = plt.subplots()

    for i in range(len(angles)):
        angles[i] = str(angles[i])

    ax.plot(angles, dda, label=DDA)
    ax.plot(angles, br_int, label=BR_INT)
    ax.plot(angles, br_float, label=BR_FLOAT)
    ax.plot(angles, br_antial, label=BR_ANTIALIASED)
    ax.plot(angles, wu, label=WU)
    ax.legend()

    plt.ylabel("Количество ступенек. (длина линии " + str(LENGTH) + ")")
    plt.xlabel("Углы в градусах")
    plt.show()