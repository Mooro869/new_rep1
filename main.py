from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
import random

from window import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('01.ui', self)
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)
        self.coords = []
        self.sceen_size = [680, 480]

    def draw(self):
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, self.sceen_size[0] - 100), random.randint(100, self.sceen_size [1] - 100)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())