from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from src.const import *
import src.view

class RootWindow(Tk):
    """
        Representation of root program window.
    """

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        img = PhotoImage(file="icon.png")
        self.iconphoto(True, img)

        self.minsize(1, 1)
        self["bg"] = BG_COLOR
        self.title("Drawing line")

        self.frame_actions = Frame()
        self.frame_actions["bg"] = BG_COLOR
        self.frame_actions.pack(side = RIGHT)

        self.frame_func = Frame()
        self.frame_func["bg"] = BG_COLOR

        #choosing algorithms

        self.frame_algorithm = Frame(self.frame_func)
        self.frame_algorithm["bg"] = BG_COLOR
        self.frame_algorithm.pack()

        Label(self.frame_algorithm, bg=BG_COLOR, fg=TEXT_COLOR, font=HEADING_FONT,\
            text = "Выбор алгоритма:").grid(row = 0, column = 0, pady=5)

        self.combo_box = Combobox(self.frame_algorithm)
        self.combo_box['values'] = (DDA, BR_INT, BR_FLOAT, BR_ANTIALIASED, WU, LIB_FUNC)  
        self.combo_box.current(0)
        self.combo_box.grid(column=0, row=1)
        # self.combo_box.bind("<Button-1>", lambda event,
        #                     combobox=self.combo_box: src.view.check_lb(event, ROOT))

        Label(self.frame_algorithm, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 5, column = 0, pady=10)

        #choosing bg color

        self.frame_choose_bg_color = Frame(self.frame_func)
        self.frame_choose_bg_color["bg"] = BG_COLOR
        self.frame_choose_bg_color.pack()

        Label(self.frame_choose_bg_color, bg=BG_COLOR, fg=TEXT_COLOR, font=HEADING_FONT,\
            text = "Выбор цвета фона:").grid(row = 0, column = 0, columnspan = 7, pady=5)

        self.v_bg = IntVar()
        self.v_bg.set(6)

        Radiobutton(self.frame_choose_bg_color, 
                  text=GREY,
                  bg = GREY,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, GREY),
                  value=0).grid(row = 1, column = 0)

        Radiobutton(self.frame_choose_bg_color, 
                  text=RED,
                  bg = RED,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, RED),
                  value=1).grid(row = 1, column = 1)

        Radiobutton(self.frame_choose_bg_color, 
                  text=YELLOW,
                  bg = YELLOW,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, YELLOW),
                  value=2).grid(row = 1, column = 2)

        Radiobutton(self.frame_choose_bg_color, 
                  text=GREEN,
                  bg = GREEN,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, GREEN),
                  value=3).grid(row = 1, column = 3)

        Radiobutton(self.frame_choose_bg_color, 
                  text=BLUE,
                  bg = BLUE,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, BLUE),
                  value=4).grid(row = 1, column = 4)

        Radiobutton(self.frame_choose_bg_color, 
                  text=BLACK,
                  bg = BLACK,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, BLACK),
                  value=5).grid(row = 1, column = 5)

        Radiobutton(self.frame_choose_bg_color, 
                  text=WHITE,
                  bg = WHITE,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, WHITE),
                  value=6).grid(row = 1, column = 6)

        Radiobutton(self.frame_choose_bg_color, 
                  text=WHITE,
                  bg = WHITE,
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_bg, 
                  command=lambda:src.view.change_canv_bg(ROOT, WHITE),
                  value=6).grid(row = 1, column = 6)
                  
        Label(self.frame_func, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).pack()

        # choosing pencil color

        self.frame_choose_pen_color = Frame(self.frame_func)
        self.frame_choose_pen_color["bg"] = BG_COLOR
        self.frame_choose_pen_color.pack()

        Label(self.frame_choose_pen_color, bg=BG_COLOR, fg=TEXT_COLOR, font=HEADING_FONT,\
            text = "Выбор цвета построения:").grid(row = 0, column = 0, columnspan = 7, pady=5)

        self.v_pen = IntVar()
        self.v_pen.set(5)

        Radiobutton(self.frame_choose_pen_color, 
                  text="Grey",
                  bg = "Grey",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=0).grid(row = 1, column = 0)

        Radiobutton(self.frame_choose_pen_color, 
                  text="Red",
                  bg = "Red",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=1).grid(row = 1, column = 1)

        Radiobutton(self.frame_choose_pen_color, 
                  text="Yellow",
                  bg = "Yellow",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=2).grid(row = 1, column = 2)

        Radiobutton(self.frame_choose_pen_color, 
                  text="Green",
                  bg = "Green",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=3).grid(row = 1, column = 3)

        Radiobutton(self.frame_choose_pen_color, 
                  text="Blue",
                  bg = "Blue",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=4).grid(row = 1, column = 4)

        Radiobutton(self.frame_choose_pen_color, 
                  text="Black",
                  bg = "Black",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=5).grid(row = 1, column = 5)

        Radiobutton(self.frame_choose_pen_color, 
                  text="White",
                  bg = "White",
                  indicatoron = 0,
                  width = 5,
                  variable=self.v_pen, 
                  #command=ShowChoice,
                  value=6).grid(row = 1, column = 6)

        Label(self.frame_func, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).pack()


        # input points

        self.frame_input_points = Frame(self.frame_func)
        self.frame_input_points["bg"] = BG_COLOR
        self.frame_input_points.pack()

        Label(self.frame_input_points, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Координаты отрезка:").grid(row = 0,\
            column = 0, columnspan=4, pady=10)

        Label(self.frame_input_points, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Хн").grid(row = 1, column = 0)
        
        Label(self.frame_input_points, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Yн").grid(row = 1, column = 1)

        Label(self.frame_input_points, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Хк").grid(row = 1, column = 2)
        
        Label(self.frame_input_points, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Yк").grid(row = 1, column = 3)

        self.entry_x_start = Entry(self.frame_input_points, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_x_start.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_x_start.grid(row = 2, column = 0, pady = 10)

        self.entry_y_start = Entry(self.frame_input_points, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_y_start.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_y_start.grid(row = 2, column = 1, pady = 10)

        self.entry_x_end = Entry(self.frame_input_points, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_x_end.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_x_end.grid(row = 2, column = 2, pady = 10)

        self.entry_y_end = Entry(self.frame_input_points, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_y_end.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_y_end.grid(row = 2, column = 3, pady = 10)

        self.btn_draw_line = Button(self.frame_input_points, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Нарисовать отрезок", \
            highlightbackground=FRAME_COLOR, command=lambda: src.view.draw(ROOT))
        self.btn_draw_line.grid(row=3, column=0, columnspan=4, pady = 10)

        Label(self.frame_input_points, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 4, column = 0, columnspan=4, pady=10)



        # rotate
        self.frame_spectrum = Frame(self.frame_func)
        self.frame_spectrum["bg"] = BG_COLOR
        self.frame_spectrum.pack()

        Label(self.frame_spectrum, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Параметры пучка:").grid(row = 0, \
            column = 0, columnspan=2, pady=10)
    
        Label(self.frame_spectrum, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Длина отрезка").grid(row = 1, column = 0)
        
        Label(self.frame_spectrum, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Шаг (°)").grid(row = 1, column = 1)
        

        self.entry_line_len = Entry(self.frame_spectrum, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_line_len.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_line_len.grid(row = 2, column = 0, pady = 10, padx=4)

        self.entry_angle = Entry(self.frame_spectrum, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_angle.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_angle.grid(row = 2, column = 1, pady = 10, padx=4)

        self.btn_draw_spectrum = Button(self.frame_spectrum, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Нарисовать пучок", \
            highlightbackground=FRAME_COLOR, command=lambda: src.view.draw_bunch(ROOT))
        self.btn_draw_spectrum.grid(row=3, column=0, columnspan=3, pady = 10, padx=4)
        
        Label(self.frame_spectrum, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "").grid(row = 4, column = 0, columnspan=2, pady=5)

        # back and clear buttons

        self.btn_сompare_algorithms = Button(self.frame_func, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "Сравнить алгоритмы", highlightbackground=FRAME_COLOR, \
            command=lambda: src.view.compare_algorithms(ROOT)) #, state=disabled
        self.btn_сompare_algorithms.pack()

        self.btn_сompare_stepping = Button(self.frame_func, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "Сравнить ступенчатость", highlightbackground=FRAME_COLOR, \
            command=lambda: src.view.smoth_analyze(ROOT)) #, state=disabled
        self.btn_сompare_stepping.pack()

        self.btn_clear = Button(self.frame_func, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "Очистить", highlightbackground=FRAME_COLOR,\
            command=lambda: src.view.clean_canvas(ROOT))
        self.btn_clear.pack()

        self.frame_func.pack(side = LEFT)

        ###

        #frame with canvas
        ###

        self.frame_canvas = Frame(self.frame_actions)
        self.frame_canvas["bg"] = BG_COLOR

        self.canv = Canvas(self.frame_canvas, width=CANV_X, height=CANV_Y, bg='white', highlightbackground = SALAD_COLOR)
        self.canv.pack(side=BOTTOM)


        self.frame_canvas.pack()



if __name__ == "__main__":
    ROOT = RootWindow()
#    fill_entries(ROOT)
    ROOT.mainloop()
