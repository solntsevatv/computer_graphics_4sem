from tkinter import *
from tkinter import scrolledtext
from src.points import *
from src.draw import *
from src.colors import *
import emoji

points_x = []
points_y = []

class RootWindow(Tk):
    """
        Representation of root program window.
    """

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        img = PhotoImage(file="icon.png")

        self.minsize(1, 1)
        #self.resizable(0, 0)
        self.iconphoto(True, img)
        self["bg"] = BG_COLOR
        self.title("Find minimal area")

        self.frame_actions = Frame()
        self.frame_actions["bg"] = BG_COLOR
        self.frame_actions.pack(side = RIGHT)

        # frame with buttons
        ###
        self.frame_buttons = Frame(self.frame_actions)
        self.frame_buttons["bg"] = BG_COLOR

        btn_num = 5

        self.btn_add_point = Button(self.frame_buttons, text="\U00002795 Добавить точку",\
            bg=COMPONENT_BG_COLOR, \
            fg = SALAD_COLOR, \
            command = lambda:add_point(self, points_x, points_y),\
            highlightbackground = SALAD_COLOR, \
            font=FONT)  
        self.btn_add_point.grid(column=0, row=0)


        self.btn_change_point = Button(self.frame_buttons, text="\U00002795 Изменить точку",\
            bg=COMPONENT_BG_COLOR, \
            fg = SALAD_COLOR, \
            command = lambda:change_point(self, points_x, points_y),\
            highlightbackground = SALAD_COLOR, \
            font=FONT)  
        self.btn_change_point.grid(column=1, row=0)


        self.btn_del_point = Button(self.frame_buttons, text="— Удалить точку",\
            bg=COMPONENT_BG_COLOR, \
            fg = SALAD_COLOR, \
            command = lambda:del_point(self, points_x, points_y), \
            highlightbackground = SALAD_COLOR, \
            font=FONT) 
        self.btn_del_point.grid(column=2, row=0)


        self.btn_del_all = Button(self.frame_buttons, text=emoji.emojize("X Очистить всё"),\
            bg=COMPONENT_BG_COLOR, \
            fg = SALAD_COLOR, \
            command = lambda:del_all(self, points_x, points_y), \
            highlightbackground = SALAD_COLOR, \
            font=FONT)  
        self.btn_del_all.grid(column=3, row=0)


        self.btn_solve = Button(self.frame_buttons, text=emoji.emojize(":pencil: Решить задачу"),\
            bg=COMPONENT_BG_COLOR, \
            fg = SALAD_COLOR, \
            command=lambda: draw_figures(self, points_x, points_y), \
            highlightbackground = SALAD_COLOR, \
            font=FONT)  
        self.btn_solve.grid(column=4, row=0)  


        self.frame_buttons.pack()

        #change button sizes

        self.frame_buttons.update()
        self.btn_add_point.configure(width = int(self.frame_buttons.winfo_width() / btn_num * PX_TO_TXT))
        self.btn_change_point.configure(width = int(self.frame_buttons.winfo_width() / btn_num * PX_TO_TXT))
        self.btn_del_point.configure(width = int(self.frame_buttons.winfo_width() / btn_num * PX_TO_TXT))
        self.btn_del_all.configure(width = int(self.frame_buttons.winfo_width() / btn_num * PX_TO_TXT))
        self.btn_solve.configure(width = int(self.frame_buttons.winfo_width() / btn_num * PX_TO_TXT))
        ###


        # frame with terms
        ###

        self.frame_terms = Frame()
        self.frame_terms["bg"] = BG_COLOR


        self.txt_task = Text(self.frame_terms, width=31, height=7, wrap = WORD, \
            bg=COMPONENT_BG_COLOR, fg = TEXT_COLOR, \
            highlightbackground = FRAME_COLOR, font=FONT)
        self.txt_task.insert(INSERT, 'Задание:\n')
        self.txt_task.insert(INSERT, 'На плоскости дано множество точек. ' +\
                        'Найти такой треугольник с вершинами в этих точках, у которого ' +\
                        'разность площадей описанного круга и треугольника минимальна.')
        self.txt_task.configure(state='disabled')
        self.txt_task.grid(column = 0, row = 0)


        self.txt_terms = Text(self.frame_terms, width=31, height=4, wrap = WORD, \
            bg=COMPONENT_BG_COLOR, fg = TEXT_COLOR, \
            highlightbackground = FRAME_COLOR, font=FONT)
        self.txt_terms.insert(INSERT, 'Обозначения:\n')
        self.txt_terms.insert(INSERT, 'Бирюзовый цвет - стороны треугольника.\n' +\
                                    'Салатовый цвет - окружность.')
        self.txt_terms.grid(column = 0, row = 1)


        self.txt = scrolledtext.ScrolledText(self.frame_terms, width=29, height=30, wrap = WORD, \
            bg=COMPONENT_BG_COLOR, fg = TEXT_COLOR, \
            highlightbackground = FRAME_COLOR, font=FONT) 
        self.txt.insert(INSERT, 'Введённые координаты точек:\n') 
        self.txt.grid(column=0, row=2)


        self.frame_terms.pack(side = LEFT)

        ###

        #frame with canvas
        ###

        self.frame_canvas = Frame(self.frame_actions)
        self.frame_canvas["bg"] = BG_COLOR

        self.canv = Canvas(self.frame_canvas, width=CANV_X, height=CANV_Y, bg='black', highlightbackground = SALAD_COLOR)
        self.canv.pack()

        self.frame_canvas.pack()



if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
