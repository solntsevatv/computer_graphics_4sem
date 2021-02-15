from tkinter import messagebox as mb
from tkinter import *
from src.colors import *

EPS = 1e-6

FONT = 'helvetica 14'

def del_coord(x, y, points_x, points_y):
    ind_point_to_del = find_coord(x, y, points_x, points_y)
    points_x.pop(ind_point_to_del)
    points_y.pop(ind_point_to_del)

def find_coord(x, y, points_x, points_y):
    n = len(points_x)
    for i in range(n):
        if (abs(points_x[i] - x) < EPS and abs(points_y[i] - y) < EPS):
            return i
    return -1


def change_point(root, points_x, points_y):
    def change_point_by_num():
        try:
            x = float(entry_x.get())
            y = float(entry_y.get())

            ind = int(entry_num.get()) - 1

            if (ind < 0 or ind >= len(points_x)):
                mb.showerror("Ошибка", "Точка с таким номером не существует.")
            else:
                if (find_coord(x, y, points_x, points_y) != -1):
                    mb.showerror("Ошибка", "Точка с такими координатами уже существует.")
                    return

                points_x[ind] = x
                points_y[ind] = y
                update_coords_table(root, points_x, points_y)

        except ValueError:
            mb.showerror("Ошибка", "Одно из чисел или оба некорректны. Введите снова.")
            

    change_point = Toplevel()
    change_point.title("Изменить точку")
    change_point.configure(bg = BG_COLOR)

    frame_point_num = Frame(change_point)
    frame_point_num["bg"] = BG_COLOR
    frame_point_num.pack(pady = 7)

    Label(frame_point_num, \
        text = "Введите номер точки, которую нужно изменить", 
        pady = 3,
        bg = BG_COLOR,
        fg = TEXT_COLOR, 
        font=FONT).pack(side = TOP)

    entry_num = Entry(frame_point_num)
    entry_num.pack(side = TOP)

    frame_coord = Frame(change_point)
    frame_coord["bg"] = BG_COLOR
    frame_coord.pack(pady = 7)

    Label(frame_coord, \
        text = "Введите изменённые координаты", \
        pady = 3,
        bg = BG_COLOR,
        fg = TEXT_COLOR,
        font=FONT).pack(side = TOP)

    Label(frame_coord, \
        text = "  X =  ", \
        bg = BG_COLOR,
        fg = TEXT_COLOR,
        font=FONT).pack(side = LEFT)
    
    entry_x = Entry(frame_coord)
    entry_x.pack(side = LEFT)

    Label(frame_coord, \
        text = "  Y = " , \
        bg = BG_COLOR,
        fg = TEXT_COLOR,
        font=FONT).pack(side = LEFT)
    
    entry_y = Entry(frame_coord)
    entry_y.pack(side = LEFT, padx = 4)

    but_ok = Button(change_point, \
        text = "Ввод", \
        bg = BG_COLOR,
        fg = TEXT_COLOR,
        font=FONT,
        command= change_point_by_num)
    but_ok.pack(pady = 7)


def coords_to_text(points_x, points_y):
    text = ""
    for i in range(len(points_x)):
        text += f"{i + 1}. ({points_x[i]}; {points_y[i]})\n"
    return text

def update_coords_table(root, points_x, points_y):
    """
        Updates table with coordinates
    """

    text = coords_to_text(points_x, points_y)
    root.txt.delete(1.0, END)
    root.txt.insert(INSERT, 'Введённые координаты точек:\n')
    root.txt.insert(INSERT, text)
    root.txt.update()

def create_coord_win(title, root, points_x, points_y):
    def add_new_point(event):
        try:
            x = float(entry_x.get())
            y = float(entry_y.get())

            if (find_coord(x, y, points_x, points_y) != -1):
                mb.showerror("Ошибка", "Точка с такими координатами уже существует.")
            else:
                points_x.append(x)
                points_y.append(y)
                update_coords_table(root, points_x, points_y)
        except ValueError:
            mb.showerror("Ошибка", "Одно из чисел или оба некорректны. Введите снова.")
            

    def del_choosen_point(event):
        try:
            text = root.txt.get(1.0, END)
            str_coord = "({}; {})\n".format(float(entry_x.get()), float(entry_y.get()))
            if (text.find(str_coord) != -1):
                del_coord(float(entry_x.get()), float(entry_y.get()), points_x, points_y)
                update_coords_table(root, points_x, points_y)
            else:
                mb.showerror("Ошибка", "Не существует точки с такими координатами. Введите снова.")
        except ValueError:
            mb.showerror("Ошибка", "Одно из чисел или оба некорректны. Введите снова.")

    add_point = Toplevel()
    add_point.title(title)
    add_point.configure(bg = BG_COLOR)

    frame_coord = Frame(add_point)
    frame_coord["bg"] = BG_COLOR
    frame_coord.pack(pady = 7)

    Label(frame_coord, \
        text = "  X =  ", \
        bg = BG_COLOR,
        fg = TEXT_COLOR).pack(side = LEFT)
    
    entry_x = Entry(frame_coord)
    entry_x.pack(side = LEFT)

    Label(frame_coord, \
        text = "  Y = " , \
        bg = BG_COLOR,
        fg = TEXT_COLOR).pack(side = LEFT)
    
    entry_y = Entry(frame_coord)
    entry_y.pack(side = LEFT, padx = 4)

    but_ok = Button(add_point, \
        text = "Ввод", \
        bg = BG_COLOR,
        fg = TEXT_COLOR,)
    but_ok.pack(pady = 7)

    if (title == "Добавить точку"):
        but_ok.bind("<Button-1>", add_new_point)
    elif (title == "Удалить точку"):
        but_ok.bind("<Button-1>", del_choosen_point)


def add_point(root, points_x, points_y):
    create_coord_win("Добавить точку", root, points_x, points_y)

def del_point(root, points_x, points_y):
    create_coord_win("Удалить точку", root, points_x, points_y)

def del_all(root, points_x, points_y):
    root.canv.delete("all")
    points_x.clear()
    points_y.clear()
    update_coords_table(root, points_x, points_y)