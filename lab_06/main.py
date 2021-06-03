from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QColorDialog
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPointF

from time import time, sleep
import sys
from copy import deepcopy

edge_color = Qt.black
fill_color = Qt.blue
bg_color = Qt.white
point_seed = False
circle = False

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = myScene(0, 0, 561, 581)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(bg_color)
        self.lock.clicked.connect(lambda: lock(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.paint.clicked.connect(lambda: fill_with_seed(self))
        self.addpoint.clicked.connect(lambda: add_point_by_btn(self))
        self.time.clicked.connect(lambda: measure_time(self))
        self.PickColor.clicked.connect(lambda: openColorDialog(self))
        self.add_seed_point.clicked.connect(lambda: set_flag_seed(self))
        self.add_circle.clicked.connect(lambda: set_flag_cir(self))

        self.edges = []
        self.seed_p = [-1, -1]
        self.point_now = None
        self.point_lock = None
        self.pen = QPen(edge_color)
        self.delay.setChecked(False)

class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        if point_seed or circle:
            get_pixel(event.scenePos())
        else:
            add_point(event.scenePos())

def openColorDialog(self):
    global fill_color 
    fill_color = QColorDialog.getColor()
    self.pen = QPen(fill_color)

def set_flag_seed(win):
    global point_seed
    point_seed = True
    win.lock.setDisabled(True)
    win.erase.setDisabled(True)
    win.paint.setDisabled(True)
    win.add_circle.setDisabled(True)
    win.PickColor.setDisabled(True)
    win.time.setDisabled(True)

def set_flag_cir(win):
    global circle
    circle = True
    win.lock.setDisabled(True)
    win.erase.setDisabled(True)
    win.paint.setDisabled(True)
    win.addpoint.setDisabled(True)
    win.add_circle.setDisabled(True)
    win.PickColor.setDisabled(True)
    win.time.setDisabled(True)

def add_row(win):
    win.table.insertRow(win.table.rowCount())

def add_point(point):
    global w, point_seed
    if not point_seed:
        add_row(w)
        i = w.table.rowCount() - 1
        item_x = QTableWidgetItem("{0}".format(point.x()))
        item_y = QTableWidgetItem("{0}".format(point.y()))
        w.table.setItem(i, 0, item_x)
        w.table.setItem(i, 1, item_y)

        if w.point_now is None:
            w.point_now = point
            w.point_lock = point
        else:
            w.edges.append([w.point_now.x(), w.point_now.y(),
                            point.x(), point.y()])
            w.point_now = point
            item_x = w.table.item(i-1, 0)
            item_y = w.table.item(i-1, 1)
            w.scene.addLine(point.x(), point.y(), float(item_x.text()), float(item_y.text()), w.pen)
    else:
        p = QPointF(point.x(), point.y())
        get_pixel(p)


def lock(win):
    if win.point_now != None:
        win.edges.append([win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y()])
        win.scene.addLine(win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y(), w.pen)
        win.point_now = None


def clean_all(win):
    win.scene.clear()
    win.table.clear()
    win.image.fill(bg_color)
    win.edges = []
    win.point_now = None
    win.point_lock = None
    r = win.table.rowCount()
    for i in range(r, -1, -1):
        win.table.removeRow(i)


def draw_edges(win, edges):
    p = QPainter()
    p.begin(win.image)
    p.setPen(QPen(edge_color))
    for ed in edges:
        #win.scene.addLine(ed[0], ed[1], ed[2], ed[3], win.pen)
        p.drawLine(int(ed[0]), int(ed[1]), int(ed[2]), int(ed[3]))
    p.end()

def draw_circle(win, radius, point):
    p = QPainter()
    p.begin(win.image)
    p.setPen(QPen(QColor(edge_color)))
    p.drawEllipse(point.x() - radius, point.y() - radius, radius * 2, radius * 2)
    for ed in win.edges:
        p.drawLine(int(ed[0]), int(ed[1]), int(ed[2]), int(ed[3]))
    p.end()

def delay():
    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 1)

def find_max_x(ed):
    x_max = None
    for i in range(len(ed)):
        if x_max is None or ed[i][0] > x_max:
            x_max = ed[i][0]

        if x_max is None or ed[i][2] > x_max:
            x_max = ed[i][2]

    return x_max


def fill_with_seed(win):
    if (win.seed_p[0] == -1 and win.seed_p[1] == -1):
        return

    pix = QPixmap()

    paint = QPainter()
    paint.begin(win.image)

    stack = []

    edge = QColor(edge_color).rgb()
    fill = QColor(fill_color).rgb()
    #paint.setPen(QPen(fill))

    z = QPointF(win.seed_p[0], win.seed_p[1])
    stack.append(z)

    # пока стек не пуст

    while stack:
        # извлечение пикселя (х,у) из стека
        p = stack.pop()
        x = int(p.x())
        y = int(p.y())
        # xt = x, запоминаем абсицссу
        xt = p.x()
        # цвет(х,у) = цвет закраски
        win.image.setPixel(x, y, fill)
        # заполняем интервал слева от затравки
        x -= 1
        while win.image.pixel(x, y) != edge and x >= 0:
            win.image.setPixel(x, y, fill)
            x -= 1


        # сохраняем крайний слева пиксел
        xl = x + 1
        x = xt
        # заполняем интервал справа от затравки
        x = x + 1

        while win.image.pixel(x, y) != edge:
            win.image.setPixel(x, y, fill)
            x = x + 1
        # сохраняем крайний справа пиксел
        xr = x - 1
        y = y + 1
        x = xl
        # ищем затравку на строке выше
        while x <= xr:
            Fl = 0
            while win.image.pixel(x, y) != edge and  win.image.pixel(x, y) != fill and  x <= xr:
                if Fl == 0:
                    Fl = 1
                x += 1

            if Fl == 1:
                if x == xr and win.image.pixel(x, y) != fill and win.image.pixel(x, y) != edge:
                    stack.append(QPointF(x, y))
                else:
                    stack.append(QPointF(x - 1, y))

            xt = x
            while (win.image.pixel(x, y) == edge or win.image.pixel(x, y) == fill) and x < xr:
                x += 1

            if x == xt:
                x += 1

        y = y - 2
        x = xl
        while x <= xr:
            Fl = 0
            while win.image.pixel(x, y) != edge and win.image.pixel(x, y) != fill and x <= xr:
                if Fl == 0:
                    Fl = 1
                x += 1

            if Fl == 1:
                if x == xr and win.image.pixel(x, y) != fill and win.image.pixel(x, y) != edge:
                    stack.append(QPointF(x, y))
                else:
                    stack.append(QPointF(x - 1, y))

            xt = x
            while (win.image.pixel(x, y) == edge or win.image.pixel(x, y) == fill) and x < xr:
                x += 1

            if x == xt:
                x += 1

        if win.delay.isChecked():
            delay()
            pix.convertFromImage(win.image)
            win.scene.addPixmap(pix)

    if not win.delay.isChecked():
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)


def add_point_by_btn(win):
    x = win.x.value()
    y = win.y.value()
    p = QPointF()
    p.setX(x)
    p.setY(y)
    add_point(p)

def get_pixel(point):
    global w, point_seed, circle
    pix = QPixmap()

    if circle:
        r = w.radius.value()
        draw_circle(w, r, point)
        circle = False

    if point_seed:
        w.seed_p[0] = point.x()
        w.seed_p[1] = point.y()
        draw_edges(w, w.edges)
        point_seed = False
        
    pix.convertFromImage(w.image)
    w.scene.addPixmap(pix)
    w.lock.setDisabled(False)
    w.erase.setDisabled(False)
    w.paint.setDisabled(False)
    w.addpoint.setDisabled(False)
    w.add_circle.setDisabled(False)
    w.PickColor.setDisabled(False)
    w.time.setDisabled(False)


def measure_time(win):
    global fill_color
    curr_col = fill_color
    fill_color = Qt.white

    start = time()
    fill_with_seed(win)
    end = time()

    fill_color = curr_col

    QMessageBox.information(win, 'Временная характеристика', "Время, затраченное на закраску: {:.2e} сек.".format((end - start) / 1000), QMessageBox.Ok)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
