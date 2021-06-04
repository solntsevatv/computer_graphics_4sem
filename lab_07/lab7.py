from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QTransform
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint
import time

red = Qt.red
blue = Qt.blue

INVISIBLE = 0
VISIBLE = 1

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window7.ui", self)
        self.scene = Scene(0, 0, 621, 671)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(621, 671, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(Qt.white)
        self.sections.clicked.connect(lambda : set_sections(self))
        self.clean.clicked.connect(lambda: clean_all(self))
        self.paint.clicked.connect(lambda: clipping(self))
        self.rect.clicked.connect(lambda: set_rect(self))
        self.ect.clicked.connect(lambda: add_sections(self))
        self.lines = []
        self.cutter = None
        self.clip = None
        self.point_now = None
        self.input_sections = False
        self.input_rect = False
        self.pen = QPen(red)


class Scene(QtWidgets.QGraphicsScene):
    # добавить точку по щелчку мыши
    def mousePressEvent(self, event):
        add_point(event.scenePos())
    # добавить прямоугольник
    def mouseMoveEvent(self, event):
        global w
        if not w.input_rect:
            return

        if w.cutter is None:
            w.cutter = event.scenePos()
        else:
            self.removeItem(self.itemAt(w.cutter, QTransform()))
            p = event.scenePos()
            self.addRect(w.cutter.x(), w.cutter.y(), abs(w.cutter.x() - p.x()), abs(w.cutter.y() - p.y()))

def set_sections(win):
    if win.input_sections:
        win.input_sections = False
        win.rect.setDisabled(False)
        win.clean.setDisabled(False)
        win.paint.setDisabled(False)
        win.ect.setDisabled(False)
    else:
        win.input_sections = True
        win.rect.setDisabled(True)
        win.clean.setDisabled(True)
        win.paint.setDisabled(True)
        win.ect.setDisabled(True)


def set_rect(win):
    if win.input_rect:
        win.input_rect = False
        win.sections.setDisabled(False)
        win.clean.setDisabled(False)
        win.paint.setDisabled(False)
        win.ect.setDisabled(False)
    else:
        win.input_rect = True
        win.sections.setDisabled(True)
        win.clean.setDisabled(True)
        win.paint.setDisabled(True)
        win.ect.setDisabled(True)

# Добавить строку с координатами в таблицу
def add_row(win):
    win.table.insertRow(win.table.rowCount())

# Добавить точку
def add_point(point):
    global w
    if not w.input_sections:
        return

    if w.point_now is None:
        w.point_now = point
    else:
        w.lines.append([[w.point_now.x(), w.point_now.y()],
                        [point.x(), point.y()]])

        add_row(w)
        i = w.table.rowCount() - 1
        item_b = QTableWidgetItem("[{:.1f}, {:.1f}]".format(w.point_now.x(), w.point_now.y()))
        item_e = QTableWidgetItem("[{:.1f}, {:.1f}]".format(point.x(), point.y()))
        w.table.setItem(i, 0, item_b)
        w.table.setItem(i, 1, item_e)
        w.scene.addLine(w.point_now.x(), w.point_now.y(), point.x(), point.y(), w.pen)
        w.point_now = None

# Сброс всех ранее введённых данных
def clean_all(win):
    win.scene.clear()
    win.table.clear()
    win.lines = []
    win.image.fill(Qt.white)
    row_count = win.table.rowCount()
    for i in range(row_count, -1, -1):
        win.table.removeRow(i)

# Добавление вертикальных и горизонтальных прямых на прямоугольнике
def add_sections(win):
    if win.cutter is None:
        QMessageBox.warning(win, "Внимание!", "Не введен отсекатель!")
        return
    buf = win.scene.itemAt(win.cutter, QTransform())
    if buf is None:
        QMessageBox.warning(win, "Внимание!", "Не введен отсекатель!")
    else:
        buf = buf.rect()
        win.clip = [buf.left(), buf.right(), buf.top(),  buf.bottom()]

        t = abs(win.clip[2] - win.clip[3]) * 0.8
        k = abs(win.clip[0] - win.clip[1]) * 0.8
        # задаем граничные отрезки
        win.pen.setColor(red)
        w.lines.append([[win.clip[0], win.clip[2] + t],  [win.clip[0], win.clip[3] - t]])
        add_row(w)
        i = w.table.rowCount() - 1
        item_b = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[0], win.clip[2] + t))
        item_e = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[0], win.clip[3] - t))
        w.table.setItem(i, 0, item_b)
        w.table.setItem(i, 1, item_e)
        win.scene.addLine(win.clip[0], win.clip[2] + t,  win.clip[0], win.clip[3] - t, win.pen)

        w.lines.append([[win.clip[1], win.clip[2] + t],  [win.clip[1], win.clip[3] - t]])
        add_row(w)
        i = w.table.rowCount() - 1
        item_b = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[1], win.clip[2] + t))
        item_e = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[1], win.clip[3] - t))
        w.table.setItem(i, 0, item_b)
        w.table.setItem(i, 1, item_e)
        win.scene.addLine(win.clip[1], win.clip[3] - t,  win.clip[1], win.clip[2] + t, win.pen)

        w.lines.append([[win.clip[0] + k, win.clip[2]], [win.clip[1] - k, win.clip[2]]])
        add_row(w)
        i = w.table.rowCount() - 1
        item_b = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[0] + k, win.clip[2]))
        item_e = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[1] - k, win.clip[2]))
        w.table.setItem(i, 0, item_b)
        w.table.setItem(i, 1, item_e)
        win.scene.addLine(win.clip[0] + k, win.clip[2], win.clip[1] - k, win.clip[2], win.pen)

        w.lines.append([[win.clip[0] + k, win.clip[3]], [win.clip[1] - k, win.clip[3]]])
        add_row(w)
        i = w.table.rowCount() - 1
        item_b = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[0] + k, win.clip[3]))
        item_e = QTableWidgetItem("[{:.1f}, {:.1f}]".format(win.clip[1] - k, win.clip[3]))
        w.table.setItem(i, 0, item_b)
        w.table.setItem(i, 1, item_e)
        win.scene.addLine(win.clip[0] + k, win.clip[3], win.clip[1] - k, win.clip[3], win.pen)


def get_code(point, rect):
    code = [0, 0, 0, 0]
    if point[0] < rect[0]:
        code[0] = 1
    if point[0] > rect[1]:
        code[1] = 1
    if point[1] < rect[2]:
        code[2] = 1
    if point[1] > rect[3]:
        code[3] = 1

    return code

# отсекание
def clipping(win):
    buf = win.scene.itemAt(win.cutter, QTransform()).rect()
    win.clip = [buf.left(), buf.right(), buf.top(),  buf.bottom()]
    for b in win.lines:
        pass
        win.pen.setColor(blue)
        cohen_sutherland(b, win.clip, win)
        win.pen.setColor(red)


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p

#  Видимость
def is_visible(section, rect):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""

    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(section[0], rect))
    s2 = sum(get_code(section[1], rect))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = VISIBLE
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(get_code(section[0], rect), get_code(section[1], rect))
        if l != 0:
            vis = INVISIBLE

    return vis

# Алгоритм Сазерленда-Коэна
def cohen_sutherland(section, rect, win):
    # инициализация флага
    flag = 1 # общего положения
    t = 1

    # проверка вертикальности и горизонтальности отрезка
    if abs(section[1][0] - section[0][0]) < 1e-6:
        flag = -1   # вертикальный отрезок
    else:
        # вычисление наклона
        t = (section[1][1] - section[0][1]) / (section[1][0] - section[0][0])
        if abs(t) < 1e-6:
            flag = 0   # горизонтальный

    # для каждой стороны окна
    for i in range(4):
        vis = is_visible(section, rect)
        if vis == VISIBLE:
            win.scene.addLine(section[0][0], section[0][1], section[1][0], section[1][1], win.pen)
            return
        elif vis == INVISIBLE:
            return

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(section[0], rect)
        code2 = get_code(section[1], rect)

        if code1[i] == code2[i]:
            continue

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if code1[i] == 0:
            section[0], section[1] = section[1], section[0]

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:
            if i < 2:
                section[0][1] = t * (rect[i] - section[0][0]) + section[0][1]
                section[0][0] = rect[i]
                continue
            else:
                section[0][0] = (1 / t) * (rect[i] - section[0][1]) + section[0][0]

        section[0][1] = rect[i]
    win.scene.addLine(section[0][0], section[0][1], section[1][0], section[1][1], win.pen)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
