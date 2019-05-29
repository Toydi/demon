import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.lay = QVBoxLayout()
        self.setLayout(self.lay)

        self.button = QPushButton("run")
        self.button.clicked.connect(self.on_click)
        self.lay.addWidget(self.button, 0)

        self.sub_widget = QWidget()
        self.sub_widget.sub_lay = QVBoxLayout()
        self.sub_widget.setLayout(self.sub_widget.sub_lay)

        self.lay.addWidget(self.sub_widget, 1)

        self.lay2 = UVA([(500, 500), (10, 10), (100, 100), (0, 100), (200, 300), (400, 400), (10, 10)], self)
        self.sub_widget.sub_lay.addWidget(self.lay2)

        self.lay3 = UVA([(500, 500), (400, 400), (300, 300), (200, 100), (100, 300)], self)
        self.sub_widget.sub_lay.addWidget(self.lay3)

        self.resize(1000, 1000)

    def on_click(self):
        self.lay2.run()
        self.lay3.run()


class UVA(QWidget):
    def __init__(self, locations, par, pen=QPen(Qt.black, 5, Qt.SolidLine)):
        super(QWidget, self).__init__()
        self.qp = QPainter()
        self.pen = pen

        self.par = par
        self.rw = locations[0][0]
        self.rh = locations[0][1]
        self.w = self.par.width()
        self.h = self.par.height()

        self.locations = locations[1:len(locations)]
        self.path = QPainterPath()
        self.points = []

        self.uva = QLabel(self)
        self.uva.setPixmap(QPixmap("./source/uva_icon-black.png").scaled(20, 20, Qt.KeepAspectRatio))

        self.anim = QPropertyAnimation(self.uva, b"pos")

        self.init_path()
        self.init_animation()
        self.resize(self.par.width(), self.par.height())

    def update_locations(self, locations):
        self.rw = locations[0][0]
        self.rh = locations[0][1]

        self.points = []
        self.path = QPainterPath()
        self.locations = locations[1:len(locations)]
        self.anim = QPropertyAnimation(self.uva, b"pos")
        self.init_path()
        self.init_animation()

    def resizeEvent(self, a0: QSize):
        self.w = self.par.width()
        self.h = self.par.height()
        self.resize(self.w, self.h)

    def init_path(self):
        self.w = self.par.width()
        self.h = self.par.height()
        for i in range(len(self.locations)):
            px = int(self.w * self.locations[i][0] / self.rw) + 10
            py = int(self.h * (self.rh - self.locations[i][1]) / self.rh) + 10
            if i == 0:
                self.path.moveTo(px, py)
            else:
                self.path.lineTo(px, py)
            self.points.append([px, py])
        self.uva.move(self.points[0][0]-10, self.points[0][1]-10)

    def init_animation(self):
        self.anim.setStartValue(QPointF(self.points[0][0]-10, self.points[0][1]-10))
        self.anim.setEndValue(QPointF(self.points[-1][0]-10, self.points[-1][1]-10))
        p = []
        l = 0
        for i in range(1, len(self.points)):
            u = self.points[i-1]
            v = self.points[i]
            d = math.sqrt((u[0]-v[0])*(u[0]-v[0])+(u[1]-v[1])*(u[1]-v[1]))
            l += d
            n = int(d) * 100
            for j in range(n):
                s = (j+1.0)/n
                p.append([u[0]+s*(v[0]-u[0]), u[1]+s*(v[1]-u[1])])
        self.anim.setDuration(int(l)*20)

        for i in range(len(p)):
            self.anim.setKeyValueAt(i/len(p), QPointF(p[i][0]-10, p[i][1]-10))

    def run(self):
        self.anim.start()

    def paintEvent(self, e):
        self.qp.begin(self)
        self.qp.setRenderHint(QPainter.Antialiasing)
        self.draw_path()
        self.qp.end()

    def draw_path(self):
        self.qp.setPen(self.pen)
        self.qp.drawPath(self.path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()

    print(form.lay2.points)
    print(form.lay3.points)

    form.lay2.update_locations([(500, 500), (10, 10), (100, 100), (0, 100), (200, 300), (400, 400), (10, 10)])
    form.lay3.update_locations([(500, 500), (400, 400), (300, 300), (200, 100), (100, 300)])

    print(form.lay2.points)
    print(form.lay3.points)

    form.show()
    app.exec_()
