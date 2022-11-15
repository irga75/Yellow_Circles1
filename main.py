import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        uic.loadUi('UI.ui')
        self.pushButton.clicked.connect(self.paintEvent)

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_circle(qp)
        # Завершаем рисование
        qp.end()

    def draw_circle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 0, 0))
        # Рисуем прямоугольник заданной кистью
        qp.setBrush(QColor(0, 255, 0))
        r = randint(30, 500)
        qp.drawEllipse(QPoint(randint(0, self.width()), randint(0, self.height())), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
