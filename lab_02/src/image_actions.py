"""
    Module for moving, rotating, scaling
"""

import tkinter as tk
from tkinter import messagebox
from copy import deepcopy

from src.bird import Bird
from src.colors import CANV_X, CANV_Y

EPS = 1e-6


def is_bird_the_same(Bird1, Bird2):
    if Bird1.center[0] - Bird2.center[0] > EPS or Bird1.center[1] - Bird2.center[1] > EPS:
        return False

    if Bird1.body_a - Bird2.body_a > EPS or Bird1.body_b - Bird2.body_b > EPS or \
        Bird1.head_radius - Bird2.head_radius > EPS:
        return False

    for i in range(len(Bird1.body)):
        if Bird1.body[i] - Bird2.body[i] > EPS:
            return False

    for i in range(len(Bird1.head)):
        if Bird1.head[i] - Bird2.head[i] > EPS:
            return False

    for i in range(len(Bird1.left_leg)):
        if Bird1.left_leg[i] - Bird2.left_leg[i] > EPS:
            return False

    for i in range(len(Bird1.right_leg)):
        if Bird1.right_leg[i] - Bird2.right_leg[i] > EPS:
            return False

    for i in range(len(Bird1.beak)):
        if Bird1.beak[i][0] - Bird2.beak[i][0] > EPS:
            return False
        
        if Bird1.beak[i][1] - Bird2.beak[i][1] > EPS:
            return False

    for i in range(len(Bird1.wing)):
        if Bird1.wing[i][0] - Bird2.wing[i][0] > EPS:
            return False
        
        if Bird1.wing[i][1] - Bird2.wing[i][1] > EPS:
            return False

    for i in range(len(Bird1.tail)):
        if Bird1.tail[i][0] - Bird2.tail[i][0] > EPS:
            return False
        
        if Bird1.tail[i][1] - Bird2.tail[i][1] > EPS:
            return False

    return True

def move(root, bird, history):
    """
        Move img elsewhere.
    """

    try:
        dx = float(root.entry_transfer_dx.get())
        dy = float(root.entry_transfer_dy.get())

        bird.move(dx, dy)
        root.canv.delete("all")
        bird.draw(root.canv)


        if (len(history) > 0 and not is_bird_the_same(bird, history[len(history) - 1])\
            or len(history) == 0):
            history.append(deepcopy(bird))
        check_history(root, history)
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Введите корректные вещественные числа.")


def rotate(root, bird, history):
    """
        Rotate img somehow.
    """

    try:
        rx = float(root.entry_scale_rx.get())
        ry = float(root.entry_scale_ry.get())
        angle = float(root.entry_scale_angle.get())

        bird.rotate(rx, ry, angle)
        root.canv.delete("all")
        bird.draw(root.canv)

        if (len(history) > 0 and not is_bird_the_same(bird, history[len(history) - 1])\
            or len(history) == 0):
            history.append(deepcopy(bird))
        check_history(root, history)
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Введите корректные вещественные числа.")
            

def scale(root, bird, history):
    """
        Scale img somehow.
    """

    try:
        mx = float(root.entry_scale_mx.get())
        my = float(root.entry_scale_my.get())
        kx = float(root.entry_scale_kx.get())
        ky = float(root.entry_scale_ky.get())

        bird.scale(mx, my, kx, ky)
        root.canv.delete("all")
        bird.draw(root.canv)

        if (len(history) > 0 and not is_bird_the_same(bird, history[len(history) - 1])\
            or len(history) == 0):
            history.append(deepcopy(bird))
        check_history(root, history)
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Введите корректные вещественные числа.")


def step_back(root, bird, history):
    """
        Rollback to previous state.
    """

    root.canv.delete("all")
    last_bird = history.pop()
    if history == [] or len(history) == 1:
        history.clear()
        bird.reset()
        bird.draw(root.canv)
        history.append(deepcopy(bird))
    else:
        last_bird.draw(root.canv)
    check_history(root, history)


def check_history(root, history):
    """
        Check history list.
    """

    if len(history) <= 1:
        root.btn_back.configure(state="disabled")
    else:
        root.btn_back.configure(state="normal")

def delete_all(root, bird, history):
    """
        Delete history and draw source bird
    """

    history.clear()
    root.canv.delete("all")
    bird.reset()
    bird.draw(root.canv)
    history.append(deepcopy(bird))
    check_history(root, history)
    fill_entries(root)

def fill_entries(root):
    root.entry_transfer_dx.delete(0, "end")
    root.entry_transfer_dy.delete(0, "end")
    root.entry_scale_rx.delete(0, "end")
    root.entry_scale_ry.delete(0, "end")
    root.entry_scale_angle.delete(0, "end")
    root.entry_scale_mx.delete(0, "end")
    root.entry_scale_my.delete(0, "end")
    root.entry_scale_kx.delete(0, "end")
    root.entry_scale_ky.delete(0, "end")

    root.entry_transfer_dx.insert(tk.END, "0")
    root.entry_transfer_dy.insert(tk.END, "0")
    root.entry_scale_rx.insert(tk.END, "{}".format(CANV_X // 2))
    root.entry_scale_ry.insert(tk.END, "{}".format(CANV_Y // 2))
    root.entry_scale_angle.insert(tk.END, "0")
    root.entry_scale_mx.insert(tk.END, "{}".format(CANV_X // 2))
    root.entry_scale_my.insert(tk.END, "{}".format(CANV_Y // 2))
    root.entry_scale_kx.insert(tk.END, "1")
    root.entry_scale_ky.insert(tk.END, "1")