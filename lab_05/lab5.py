from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QColorDialog
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint

from time import time, sleep
import sys
from copy import deepcopy

fill_color = Qt.black
bg_color = Qt.white

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = myScene(0, 0, 621, 671)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(621, 671, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(bg_color)
        self.lock.clicked.connect(lambda: lock(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.paint.clicked.connect(lambda: fill_by_edges(self))
        self.addpoint.clicked.connect(lambda: add_point_by_btn(self))
        self.time.clicked.connect(lambda: measure_time(self))
        self.PickColor.clicked.connect(lambda: openColorDialog(self))
        self.edges = []
        self.point_now = None
        self.point_lock = None
        self.pen = QPen(fill_color)
        self.delay.setChecked(False)

class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        add_point(event.scenePos())

def openColorDialog(self):
    global fill_color 
    fill_color = QColorDialog.getColor()
    self.pen = QPen(fill_color)

def add_row(win):
    win.table.insertRow(win.table.rowCount())

def add_point(point):
    global w
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
    pen = QPen(Qt.black)
    for ed in edges:
        win.scene.addLine(ed[0], ed[1], ed[2], ed[3], pen)
        #p.drawLine(ed[0], ed[1], ed[2], ed[3], win.pen)


def delay():
    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 1)

def find_max_x(ed):
    x_max = ed[0][0]
    for i in range(len(ed)):
        if ed[i][0] > x_max:
            x_max = ed[i][0]

        if ed[i][2] > x_max:
            x_max = ed[i][2]

    return x_max

def fill_pixel(x, y, image, painter):
    x = int(x)
    y = int(y)

    col = QColor(image.pixel(x, y))
    if col == bg_color:
        painter.setPen(QPen(fill_color))
    else:
        painter.setPen(QPen(bg_color))
    painter.drawPoint(x, y)

def fill_by_edges(win):
    if (len(win.edges) <= 2):
        QMessageBox.information(win, 'Ошибка', "Недостаточно ребер", QMessageBox.Ok)
        return

    pix = QPixmap()
    p = QPainter()
    x_max = int(find_max_x(win.edges))
    
    for ed in win.edges:
        p.begin(win.image)
        # если горизонтальное ребро - дальше
        if abs(ed[1] - ed[3]) < 1e-6:
            continue
        # иначе определяем границы сканирования
        if ed[1] > ed[3]:
            ed[1], ed[3] = ed[3], ed[1]
            ed[0], ed[2] = ed[2], ed[0]  

        y = ed[1]
        end_y = ed[3]
        dx = (ed[2] - ed[0]) / (ed[3] - ed[1])
        start_x = ed[0]+ dx

        while y < end_y:
            x = start_x
            while x < x_max:
                fill_pixel(x, y, win.image, p)
                x += 1

            start_x += dx
            y += 1

            if win.delay.isChecked():
                delay()
                pix.convertFromImage(win.image)
                win.scene.addPixmap(pix)
        
        if not win.delay.isChecked():
            pix.convertFromImage(win.image)
            win.scene.addPixmap(pix)

        p.end()

    draw_edges(win, win.edges)

def add_point_by_btn(win):
    x = win.x.value()
    y = win.y.value()
    p = QPoint()
    p.setX(x)
    p.setY(y)
    add_point(p)


def measure_time(win):
    start = time()
    fill_by_edges(win)
    end = time()
    QMessageBox.information(win, 'Временная характеристика', "Время, затраченное на закраску: {:.2e} сек.".format((end - start) / 1000), QMessageBox.Ok)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
