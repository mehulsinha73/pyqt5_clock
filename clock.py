from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Clock(QMainWindow):

    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        self.setWindowTitle('PyQt5 Clock')
        self.setGeometry(400, 400, 500, 500)
        self.setStyleSheet("background : teal; ")

        self.hPointer = QPolygon([QPoint(2, 7), QPoint(-2, 7), QPoint(-2, -65), QPoint(2, -65)])
        self.mPointer = QPolygon([QPoint(1, 7), QPoint(-1, 7), QPoint(-1, -75), QPoint(1, -75)])
        self.sPointer = QPolygon([QPoint(1, 15), QPoint(-1, 15), QPoint(-1, -85), QPoint(1, -85)])
        
        self.bColor = Qt.green
        self.sColor = Qt.red

    def paintEvent(self, event):
        rec = min(self.width(), self.height())

        tik = QTime.currentTime()
        painter = QPainter(self)

        def drawPointer(color, rotation, pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()

        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)

        painter.scale(rec / 200, rec / 200)
        painter.setPen(QtCore.Qt.NoPen)

        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)

        painter.setPen(QPen(self.bColor))

        for i in range(0, 60):
            if (i % 5) == 0:
                painter.setPen(QPen(Qt.green))
                if (i % 15) == 0:
                    painter.drawLine(80, 0, 97, 0)
                else:
                    painter.drawLine(87, 0, 97, 0)
            else:
                painter.setPen(QPen(Qt.black))
                painter.drawLine(92, 0, 97, 0)

            painter.rotate(6)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Clock()
    win.show()
    exit(app.exec_())
