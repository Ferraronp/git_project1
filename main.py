import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_ocr(qp)
            qp.end()
        self.draw = False

    def draw_ocr(self, qp):
        for i in range(randint(1, 10)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y, r = randint(100, 400), randint(100, 400), randint(25, 100)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
