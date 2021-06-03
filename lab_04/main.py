from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from src.const import *
from src.view.view import *

class RootWindow(Tk):
    """
        Representation of root program window.
    """

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        img = PhotoImage(file="icon.png")
        self.iconphoto(True, img)

        self.minsize(1, 1) 
        self.geometry('1900x1000')
        self["bg"] = BG_COLOR
        self.title("Drawing circle/ellipse")

        self.frame_actions = Frame()
        self.frame_actions["bg"] = BG_COLOR
        self.frame_actions.pack(side = RIGHT)

        self.frame_func = Frame()
        self.frame_func["bg"] = BG_COLOR


        self.frame_choose = Frame(self.frame_func)
        self.frame_choose["bg"] = BG_COLOR
        self.frame_choose.pack()

        Label(self.frame_choose, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).pack(side=BOTTOM)

        #choosing algorithms

        Label(self.frame_choose, bg=BG_COLOR, fg=TEXT_COLOR, font=HEADING_FONT,\
            text = "Выбор алгоритма:").pack()

        self.combo_box = Combobox(self.frame_choose, width = 25)
        self.combo_box['values'] = (CANON_EQ, PARAM_EQ, BRESENHAM, MIDDLE_POINT, LIB_FUNC)  
        self.combo_box.current(0)
        self.combo_box.pack()

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


        # draw circle

        self.frame_draw_circle = Frame(self.frame_func)
        self.frame_draw_circle["bg"] = BG_COLOR
        self.frame_draw_circle.pack()

        Label(self.frame_draw_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Параметры окружности:").grid(row = 0,\
            column = 0, columnspan=4, pady=5)

        Label(self.frame_draw_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Хс").grid(row = 1, column = 0)
        
        Label(self.frame_draw_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Yс").grid(row = 1, column = 1)

        Label(self.frame_draw_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "R").grid(row = 1, column = 2)
        
        self.entry_x_circle_center = Entry(self.frame_draw_circle, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_x_circle_center.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_x_circle_center.grid(row = 2, column = 0, pady = 10)

        self.entry_y_circle_center = Entry(self.frame_draw_circle, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_y_circle_center.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_y_circle_center.grid(row = 2, column = 1, pady = 10)

        self.entry_circle_radius = Entry(self.frame_draw_circle, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_circle_radius.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_circle_radius.grid(row = 2, column = 2, pady = 10)

        self.btn_draw_circle = Button(self.frame_draw_circle, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Нарисовать окружность", \
            highlightbackground=FRAME_COLOR, command=lambda: draw_circle(ROOT))
        self.btn_draw_circle.grid(row=3, column=0, columnspan=3, pady = 5)

        Label(self.frame_draw_circle, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 4, column = 0, columnspan=3, pady=5)


        # draw ellipse

        self.frame_draw_ellipse = Frame(self.frame_func)
        self.frame_draw_ellipse["bg"] = BG_COLOR
        self.frame_draw_ellipse.pack()

        Label(self.frame_draw_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Параметры эллипса:").grid(row = 0,\
            column = 0, columnspan=4, pady=5)

        Label(self.frame_draw_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Хс").grid(row = 1, column = 0)
        
        Label(self.frame_draw_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Yс").grid(row = 1, column = 1)

        Label(self.frame_draw_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "а").grid(row = 1, column = 2)

        Label(self.frame_draw_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "b").grid(row = 1, column = 3)
        
        self.entry_x_ellipse_center = Entry(self.frame_draw_ellipse, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_x_ellipse_center.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_x_ellipse_center.grid(row = 2, column = 0, pady = 10)

        self.entry_y_ellipse_center = Entry(self.frame_draw_ellipse, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_y_ellipse_center.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_y_ellipse_center.grid(row = 2, column = 1, pady = 10)

        self.entry_ellipse_a = Entry(self.frame_draw_ellipse, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_ellipse_a.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_ellipse_a.grid(row = 2, column = 2, pady = 10)

        self.entry_ellipse_b = Entry(self.frame_draw_ellipse, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_ellipse_b.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_ellipse_b.grid(row = 2, column = 3, pady = 10)

        self.btn_draw_ellipse = Button(self.frame_draw_ellipse, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Нарисовать эллипс", \
            highlightbackground=FRAME_COLOR, command=lambda: draw_ellipse(ROOT))
        self.btn_draw_ellipse.grid(row=3, column=0, columnspan=4, pady = 5)

        Label(self.frame_draw_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 4, column = 0, columnspan=4, pady=5)

        # spectrum_circle
        self.frame_spectrum_circle = Frame(self.frame_func)
        self.frame_spectrum_circle["bg"] = BG_COLOR
        self.frame_spectrum_circle.pack()

        Label(self.frame_spectrum_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Параметры спектра окружностей:").grid(row = 0, \
            column = 0, columnspan=4, pady=10)
    
        Label(self.frame_spectrum_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Rн").grid(row = 1, column = 0)
        
        Label(self.frame_spectrum_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Rк").grid(row = 1, column = 1)
        
        Label(self.frame_spectrum_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Шаг").grid(row = 1, column = 2)
        
        Label(self.frame_spectrum_circle, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "N").grid(row = 1, column = 3)

        self.entry_spectr_circle_start_r = Entry(self.frame_spectrum_circle, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_circle_start_r.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_circle_start_r.grid(row = 2, column = 0, pady = 10, padx=4)

        self.entry_spectr_circle_finish_r = Entry(self.frame_spectrum_circle, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_circle_finish_r.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_circle_finish_r.grid(row = 2, column = 1, pady = 10, padx=4)

        self.entry_spectr_circle_step = Entry(self.frame_spectrum_circle, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_circle_step.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_circle_step.grid(row = 2, column = 2, pady = 10, padx=4)

        self.entry_spectr_circle_n = Entry(self.frame_spectrum_circle, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_circle_n.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_circle_n.grid(row = 2, column = 3, pady = 10, padx=4)

        self.btn_draw_spectrum_circle = Button(self.frame_spectrum_circle, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Нарисовать пучок окружностей", \
            highlightbackground=FRAME_COLOR, command=lambda: draw_circle_spectre(ROOT))
        self.btn_draw_spectrum_circle.grid(row=3, column=0, columnspan=4, pady = 10, padx=4)
        
        Label(self.frame_spectrum_circle, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 4, column = 0, columnspan=4, pady=5)


        # spectrum ellipse
        self.frame_spectrum_ellipse = Frame(self.frame_func)
        self.frame_spectrum_ellipse["bg"] = BG_COLOR
        self.frame_spectrum_ellipse.pack()

        Label(self.frame_spectrum_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Параметры спектра эллипсов:").grid(row = 0, \
            column = 0, columnspan=4, pady=10)
    
        Label(self.frame_spectrum_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "a").grid(row = 1, column = 0)
        
        Label(self.frame_spectrum_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "b").grid(row = 1, column = 1)
        
        Label(self.frame_spectrum_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Шаг").grid(row = 1, column = 2)
        
        Label(self.frame_spectrum_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "N").grid(row = 1, column = 3)

        self.entry_spectr_ellipse_a = Entry(self.frame_spectrum_ellipse, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_ellipse_a.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_ellipse_a.grid(row = 2, column = 0, pady = 10, padx=4)

        self.entry_spectr_ellipse_b = Entry(self.frame_spectrum_ellipse, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_ellipse_b.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_ellipse_b.grid(row = 2, column = 1, pady = 10, padx=4)

        self.entry_spectr_ellipse_step = Entry(self.frame_spectrum_ellipse, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_ellipse_step.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_ellipse_step.grid(row = 2, column = 2, pady = 10, padx=4)

        self.entry_spectr_ellipse_n = Entry(self.frame_spectrum_ellipse, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_spectr_ellipse_n.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_spectr_ellipse_n.grid(row = 2, column = 3, pady = 10, padx=4)

        self.btn_draw_spectrum_ellipse = Button(self.frame_spectrum_ellipse, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Нарисовать пучок эллипсов", \
            highlightbackground=FRAME_COLOR, command=lambda: draw_ellipse_spectre(ROOT))
        self.btn_draw_spectrum_ellipse.grid(row=3, column=0, columnspan=4, pady = 10, padx=4)
        
        Label(self.frame_spectrum_ellipse, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "").grid(row = 4, column = 0, columnspan=4, pady=5)
        

        self.frame_func.pack(side = LEFT)

        ###

        #frame with buttons

        self.frame_buttons = Frame(self.frame_actions)
        self.frame_buttons["bg"] = BG_COLOR

        # buttons

        self.btn_сompare_algorithms = Button(self.frame_buttons, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "Сравнить алгоритмы", highlightbackground=FRAME_COLOR, \
            command=lambda: compare_algorithms(ROOT.canv)) #, state=disabled
        self.btn_сompare_algorithms.pack(side=LEFT)

        self.btn_clear = Button(self.frame_buttons, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "Очистить", highlightbackground=FRAME_COLOR,\
            command=lambda: clean_canvas(ROOT))
        self.btn_clear.pack(side=LEFT)


        self.frame_buttons.pack(side = TOP, pady=4)

        #frame with canvas
        ###

        self.frame_canvas = Frame(self.frame_actions)
        self.frame_canvas["bg"] = BG_COLOR

        self.canv = Canvas(self.frame_canvas, width=CANV_X, height=CANV_Y, bg='white', highlightbackground = FRAME_COLOR)
        self.canv.pack(side=BOTTOM)


        self.frame_canvas.pack()



if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()