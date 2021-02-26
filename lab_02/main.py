from tkinter import *
from tkinter import scrolledtext
from src.colors import *
from src.bird import *
from src.image_actions import *
from copy import deepcopy

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
        self.title("Converting a picture")

        self.frame_actions = Frame()
        self.frame_actions["bg"] = BG_COLOR
        self.frame_actions.pack(side = RIGHT)


        self.frame_func = Frame()
        self.frame_func["bg"] = BG_COLOR


        # move

        self.frame_transfer = Frame(self.frame_func)
        self.frame_transfer["bg"] = BG_COLOR
        self.frame_transfer.pack()

        Label(self.frame_transfer, bg=BG_COLOR, fg=TEXT_COLOR, font=HEADING_FONT,\
            text = "Перенос").grid(row = 1, column = 0, columnspan=2, pady=5)

        Label(self.frame_transfer, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "dx").grid(row = 2, column = 0)
        
        Label(self.frame_transfer, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "dy").grid(row = 2, column = 1)

        self.entry_transfer_dx = Entry(self.frame_transfer, bg=COMPONENT_BG_COLOR, fg=ENTRY_TEXT_COLOR)
        self.entry_transfer_dx.config(highlightbackground=FRAME_COLOR,font=FONT, width=15)
        self.entry_transfer_dx.grid(row = 3, column = 0, pady = 10)

        self.entry_transfer_dy = Entry(self.frame_transfer, bg = COMPONENT_BG_COLOR, fg=ENTRY_TEXT_COLOR)
        self.entry_transfer_dy.config(highlightbackground=FRAME_COLOR,font=FONT, width=15)
        self.entry_transfer_dy.grid(row = 3, column = 1, pady = 10)

        self.btn_transfer = Button(self.frame_transfer, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Перенести", highlightbackground=FRAME_COLOR,\
            command=lambda: move(ROOT, Bird, history))
        self.btn_transfer.grid(row=4,column=0, columnspan=2, pady = 10)

        Label(self.frame_transfer, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 5, column = 0, columnspan=2, pady=10)



        # scale

        self.frame_scale = Frame(self.frame_func)
        self.frame_scale["bg"] = BG_COLOR
        self.frame_scale.pack()

        Label(self.frame_scale, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Масштабирование").grid(row = 0,\
            column = 0, columnspan=4, pady=10)

        Label(self.frame_scale, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Mx").grid(row = 1, column = 0)
        
        Label(self.frame_scale, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "My").grid(row = 1, column = 1)

        Label(self.frame_scale, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "kx").grid(row = 1, column = 2)
        
        Label(self.frame_scale, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "ky").grid(row = 1, column = 3)

        self.entry_scale_mx = Entry(self.frame_scale, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_mx.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_mx.grid(row = 2, column = 0, pady = 10)

        self.entry_scale_my = Entry(self.frame_scale, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_my.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_my.grid(row = 2, column = 1, pady = 10)

        self.entry_scale_kx = Entry(self.frame_scale, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_kx.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_kx.grid(row = 2, column = 2, pady = 10)

        self.entry_scale_ky = Entry(self.frame_scale, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_ky.config(highlightbackground=FRAME_COLOR, width=8, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_ky.grid(row = 2, column = 3, pady = 10)

        self.btn_scale = Button(self.frame_scale, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Масштабировать", \
            highlightbackground=FRAME_COLOR, command=lambda: scale(ROOT, Bird, history))
        self.btn_scale.grid(row=3, column=0, columnspan=4, pady = 10)

        Label(self.frame_scale, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "_"*LINE_X).grid(row = 4, column = 0, columnspan=4, pady=10)



        # rotate
        self.frame_turn = Frame(self.frame_func)
        self.frame_turn["bg"] = BG_COLOR
        self.frame_turn.pack()

        Label(self.frame_turn, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=HEADING_FONT, text = "Поворот").grid(row = 0, \
            column = 0, columnspan=3, pady=10)
    
        Label(self.frame_turn, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Rx").grid(row = 1, column = 0)
        
        Label(self.frame_turn, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Ry").grid(row = 1, column = 1)

        Label(self.frame_turn, bg=BG_COLOR, fg=TEXT_COLOR, \
            font=FONT, text = "Угол (°)").grid(row = 1, column = 2)
        

        self.entry_scale_rx = Entry(self.frame_turn, bg=COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_rx.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_rx.grid(row = 2, column = 0, pady = 10, padx=4)

        self.entry_scale_ry = Entry(self.frame_turn, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_ry.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_ry.grid(row = 2, column = 1, pady = 10, padx=4)

        self.entry_scale_angle = Entry(self.frame_turn, bg = COMPONENT_BG_COLOR,font=FONT)
        self.entry_scale_angle.config(highlightbackground=FRAME_COLOR, width=10, fg=ENTRY_TEXT_COLOR)
        self.entry_scale_angle.grid(row = 2, column = 2, pady = 10, padx=4)

        self.btn_turn = Button(self.frame_turn, bg=COMPONENT_BG_COLOR, \
            fg=TEXT_COLOR, font=FONT, text = "Повернуть", \
            highlightbackground=FRAME_COLOR, command=lambda: rotate(ROOT, Bird, history))
        self.btn_turn.grid(row=3, column=0, columnspan=3, pady = 10, padx=4)
        
        Label(self.frame_turn, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, \
            text = "").grid(row = 4, column = 0, columnspan=3, pady=5)


        # back and clear buttons

        self.btn_back = Button(self.frame_func, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "← Назад", highlightbackground=FRAME_COLOR, \
            command=lambda: step_back(ROOT, Bird, history), state="disabled")
        self.btn_back.pack()

        self.btn_clear = Button(self.frame_func, bg=COMPONENT_BG_COLOR, width=FUNC_X,\
            fg=TEXT_COLOR, font=FONT, text = "Очистить", highlightbackground=FRAME_COLOR,\
            command=lambda: delete_all(ROOT, Bird, history))
        self.btn_clear.pack()



        self.frame_func.pack(side = LEFT)

        ###

        #frame with canvas
        ###

        self.frame_canvas = Frame(self.frame_actions)
        self.frame_canvas["bg"] = BG_COLOR

        self.canv = Canvas(self.frame_canvas, width=CANV_X, height=CANV_Y, bg='black', highlightbackground = SALAD_COLOR)
        self.canv.pack(side=BOTTOM)


        self.frame_canvas.pack()



if __name__ == "__main__":
    ROOT = RootWindow()
    history = []
    Bird = Bird()
    Bird.draw(ROOT.canv)
    history.append(deepcopy(Bird))
    fill_entries(ROOT)
    ROOT.mainloop()
