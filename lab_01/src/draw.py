from src.geom import *
from tkinter import messagebox as mb
from src.points import find_coord

TRIANGLE_FRAME_COLOR = "cyan2"
CIRCLE_FRAME_COLOR = "SpringGreen1"

PX_TO_TXT = 31 / 316

def create_figures(root, transformed_coords, circle_center, radius):
    root.canv.create_polygon(transformed_coords[0][0], transformed_coords[0][1], transformed_coords[1][0], \
        transformed_coords[1][1], transformed_coords[2][0], transformed_coords[2][1], outline=TRIANGLE_FRAME_COLOR)
    root.canv.create_oval(circle_center[0] - radius, transform_y_coord(circle_center[1] - radius), \
        circle_center[0] + radius, transform_y_coord(circle_center[1] + radius), outline = CIRCLE_FRAME_COLOR)
    root.canv.create_oval(CANV_X / 2 - 2, CANV_Y / 2 - 2, CANV_X / 2 + 2, CANV_Y / 2 + 2, outline = "white", fill = "white")

def print_coords(root, transformed_coords, coords, circle_center, circle_center_real, coord_numbers):
    y_offset = 25

    root.canv.create_text(CANV_X / 2, CANV_Y / 2 + y_offset,
        fill="white",
        font="-family {Consolas} -size 14",
        text=f"({circle_center_real[0]}; {circle_center_real[1]})")

    for i in range(3):
        txt = f"{coord_numbers[i]}) ({coords[i][0]}; {coords[i][1]})"

        # print coord behind the vertex of the triangle
        if (transformed_coords[i][1] > circle_center[1]):
            coord_y_to_print = transformed_coords[i][1] + y_offset
        # print coord above the vertex of the triangle
        else:
            coord_y_to_print = transformed_coords[i][1] - y_offset

        root.canv.create_text(transformed_coords[i][0], coord_y_to_print,
            fill="white",
            font="-family {Consolas} -size 14",
            text=txt)

def points_on_same_line(points_x, points_y):
    for i in range(len(points_x) - 2):
        if ((points_y[i + 2] - points_y[i])*(points_x[i + 1] - \
            points_x[i]) != (points_x[i + 2] - points_x[i])*(points_y[i + 1] - points_y[i])):
            return False
    return True

def draw_figures(root, points_x, points_y):
    root.canv.delete("all")
    n = len(points_x)

    if n < 3:
        mb.showerror("Ошибка", "Нельзя построить треугольник с менее чем тремя вершинами.")
        return

    min_area = 1e10
    coords = [[0, 0], [0, 0], [0, 0]]
    triangle_area = 0
    circle_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                components = find_area((points_x[i], points_y[i]), \
                (points_x[j], points_y[j]), (points_x[k], points_y[k]))

                if (components[1] - components[0] < min_area and components[1] - components[0] > 0):
                    min_area = abs(components[1] - components[0])
                    coords = [[points_x[i], points_y[i]], \
                            [points_x[j], points_y[j]], \
                            [points_x[k], points_y[k]]]
                    triangle_area = components[0]
                    circle_area = components[1]
                    radius = components[2]

    if (min_area == 1e10):
        if (points_on_same_line(points_x, points_y)):
            mb.showerror("Ошибка", "Невозможно построить треугольник, так как точки лежат на одной прямой.")
        else:
            mb.showerror("Ошибка", "Невозможно найти решение для заданных координат.")
        return

    coord_numbers = [find_coord(coords[0][0], coords[0][1], points_x, points_y) + 1, \
                    find_coord(coords[1][0], coords[1][1], points_x, points_y) + 1, \
                    find_coord(coords[2][0], coords[2][1], points_x, points_y) + 1]

    msg = ("Координаты найденного треугольника: {}) ({}; {}), {}) ({}; {}),  {}) ({}; {})." + \
        " Площадь треугольника: {:.4f}.  Площадь круга: {:.4f}. Разность между ними: {:.4f}.").format(\
        coord_numbers[0], coords[0][0], coords[0][1], coord_numbers[1], coords[1][0], coords[1][1], \
        coord_numbers[2], coords[2][0], coords[2][1], triangle_area, circle_area, circle_area - triangle_area)
    mb.showinfo("Информация", msg)

    circle_center_real = find_circle_center(coords[0][0], coords[0][1], coords[1][0], coords[1][1], \
        coords[2][0], coords[2][1])
    
    transformed_values = transform_values(coords, circle_center_real, radius)
    transformed_coords = transformed_values[0]
    circle_center = transformed_values[1]
    radius = transformed_values[2]

    create_figures(root, transformed_coords, circle_center, radius)    

    print_coords(root, transformed_coords, coords, circle_center, \
        circle_center_real, coord_numbers)
        
