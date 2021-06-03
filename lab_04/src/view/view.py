from src.const import *
import src.circledraw.canonical, src.circledraw.bresenham, src.circledraw.midpoint, src.circledraw.parametric
from src.view.util import *
from tkinter import messagebox
import colorutils as cu
import matplotlib.pyplot as plt

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

def name_to_func_circle(root, method):
    func = root.canv.create_line
    if method == CANON_EQ or method == "Каноническое\nуравнение":
        func = src.circledraw.canonical.cancircle
    elif method == PARAM_EQ or method == "Параметрическое\nуравнение":
        func = src.circledraw.parametric.parcircle
    elif method == BRESENHAM:
        func = src.circledraw.bresenham.brescircle
    elif method == MIDDLE_POINT or method == "Алгоритм средней\nточки":
        func = src.circledraw.midpoint.midpcircle
    elif method == "Библиотечная\nфункция" or method == LIB_FUNC:
        func = root.canv.create_oval
    return func

def draw_circle(root):
    """
        Draw circle using different algorithms.
    """

    method = root.combo_box.get()
    color = ind_to_color(root.v_pen.get())
    color_cu = translate_color(color)

    dots = None
    x_center, y_center, r = None, None, None
    func = None

    try:
        x_center = int(root.entry_x_circle_center.get())
        y_center = int(root.entry_y_circle_center.get())
        r = int(root.entry_circle_radius.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить целое число. Проверьте корректность ввода.")

    if method == LIB_FUNC:
        root.canv.create_oval(x_center - r, y_center - r, x_center +
                               r, y_center + r, outline=color)
        return

    func = name_to_func_circle(root, method)
    dots = func(x_center, y_center, r, color_cu)
    draw_line(root.canv, dots)

def name_to_func_ellipse(root, method):
    func = root.canv.create_line
    if method == CANON_EQ or method == "Каноническое\nуравнение":
        func = src.circledraw.canonical.canellipse
    elif method == PARAM_EQ or method == "Параметрическое\nуравнение":
        func = src.circledraw.parametric.parellipse
    elif method == BRESENHAM:
        func = src.circledraw.bresenham.bresellipse
    elif method == MIDDLE_POINT or method == "Алгоритм средней\nточки":
        func = src.circledraw.midpoint.midpellipse
    elif method == "Библиотечная\nфункция" or method == LIB_FUNC:
        func = root.canv.create_oval
    return func

def draw_ellipse(root):
    """
        Draw ellipse using different algorithms.
    """

    method = root.combo_box.get()
    color = ind_to_color(root.v_pen.get())
    color_cu = translate_color(color)

    dots = None
    x_center, y_center, a, b = None, None, None, None
    func = None

    try:
        x_center = int(root.entry_x_ellipse_center.get())
        y_center = int(root.entry_y_ellipse_center.get())
        a = int(root.entry_ellipse_a.get())
        b = int(root.entry_ellipse_b.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить целое число. Проверьте корректность ввода.")

    if method == LIB_FUNC:
        root.canv.create_oval(x_center - a, y_center - b, x_center +
                                   a, y_center + b, outline=color_cu.hex)
        return

    func = name_to_func_ellipse(root, method)
    dots = func(x_center, y_center, a, b, color_cu)
    draw_line(root.canv, dots)

def draw_circle_spectre(root):
    x_center = int(CANV_X / 2)
    y_center = int(CANV_Y / 2)
    rs1, rs2, step, n = 0, 0, 0, 0
    try:
        rs1 = int(root.entry_spectr_circle_start_r.get())
        rs2 = int(root.entry_spectr_circle_finish_r.get())
        step = int(root.entry_spectr_circle_step.get())
        n = (rs2 - rs1) // step
    except ValueError:
        try:
            rs1 = int(root.entry_spectr_circle_start_r.get())
            step = int(root.entry_spectr_circle_step.get())
            n = int(root.entry_spectr_circle_n.get())
            rs2 = rs1 + step * n
        except ValueError:
            try:
                rs1 = int(root.entry_spectr_circle_start_r.get())
                rs2 = int(root.entry_spectr_circle_finish_r.get())
                n = int(root.entry_spectr_circle_n.get())
                step = (rs2 - rs1) // n
            except ValueError:
                try:
                    rs1 = int(root.entry_spectr_circle_start_r.get())
                    step = int(root.entry_spectr_circle_step.get())
                    n = int(root.entry_spectr_circle_n.get())
                    rs2 = rs1 + step * n
                except ValueError:
                    messagebox.showerror(
                        "Ошибка ввода", "Невозможно получить число. Проверьте корректность ввода.")
                    return

    if rs1 == 0:
        rs1 = rs2 - step * n
    if rs2 == 0:
        rs2 = rs1 + step * n
    if step == 0:
        step = (rs2 - rs1) // n
    
    if (rs1 <= 0 or rs2 <= 0 or step < 0 or n <= 0):
        messagebox.showerror(
            "Ошибка ввода", "Некорректные параметры. Числа должны быть больше нуля.")
   

    method = root.combo_box.get()
    color = ind_to_color(root.v_pen.get())
    color_cu = translate_color(color)
    func = name_to_func_circle(root, method)

    for radius in range(rs1, rs2, step):
        if func == root.canv.create_oval:
            func(x_center - radius,
                    y_center - radius,
                    x_center + radius,
                    y_center + radius,
                    outline=color_cu.hex)
        else:
            dots = func(x_center, y_center, radius, color_cu)
            draw_line(root.canv, dots)

def draw_ellipse_spectre(root):
    x_center = int(CANV_X / 2)
    y_center = int(CANV_Y / 2)
    rs1, rs2, step, n = 0, 0, 0, 0
    try:
        rs1 = int(root.entry_spectr_ellipse_a.get())
        rs2 = int(root.entry_spectr_ellipse_b.get())
        step = int(root.entry_spectr_ellipse_step.get())
        n = int(root.entry_spectr_ellipse_n.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить число. Проверьте корректность ввода.")
        return

    method = root.combo_box.get()
    color = ind_to_color(root.v_pen.get())
    color_cu = translate_color(color)
    func = name_to_func_ellipse(root, method)

    for _ in range(n):
        if func == root.canv.create_oval:
            func(x_center - rs1,
                 y_center - rs2,
                 x_center + rs1,
                 y_center + rs2,
                 outline=color_cu.hex)
        else:
            dots = func(x_center, y_center, rs1, rs2, color_cu)
            draw_line(root.canv, dots)

        rs1 += step
        rs2 += step

def clean_canvas(root):
    root.canv.delete("all")

def compare_algorithms(canvas):
    """
        Show diagram with time measurements.
    """

    fig, axs = plt.subplots(2, 1)

    plt.rcParams["toolbar"] = "None"

    taken_time, radiuses = get_time(canvas)

    #circle
    axs[0].set_title('Сравнение алгоритмов построения окружностей')

    for method in taken_time:
        axs[0].plot(radiuses, taken_time[method][0], label=method)

    axs[0].set_ylabel("Затраченное время, единицы времени")
    axs[0].set_xlabel("Радиус")

    axs[0].grid()

    #ellipse

    axs[1].set_title('Сравнение алгоритмов построения эллипсов')
    for method in taken_time:
        axs[1].plot(radiuses, taken_time[method][1], label=method)

    axs[1].set_ylabel("Затраченное время, единицы времени")
    axs[1].set_xlabel("Радиус")

    axs[1].grid()

    plt.legend()
    plt.show()