#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing2")
        self.rabbit = QImage("images/frame-1.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 120, 120), QPoint(150, 130),
            QPoint(180, 120), QPoint(150, 170),
        ])

        p.setPen(QColor(0, 100, 130))
        p.setBrush(QColor(0, 100, 130))
        p.drawPie(50, 150, 100, 100, 0, 360 * 16)

        p.drawPie(150, 150, 100, 100, 0, 360 * 16)
        p.drawPie(100, 230, 100, 100, 0, 360 * 16)

        '''
        p.drawPolygon([
            QPoint(50, 400), QPoint(150, 400), QPoint(100, 800),
        ])'''

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
