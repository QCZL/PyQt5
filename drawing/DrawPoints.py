#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 21:24
# 文件名称  :  DrawPoints.py
# 开发工具  :  PyCharm


import sys
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints, self).__init__()
        self.setMinimumSize(600, 400)
        self.setWindowTitle('绘制正弦曲线')

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.black, 2))
        size = self.size()
        y_0 = size.height() // 2
        x_0 = size.width() // 2
        x_len = (size.width() - 100) // 2
        y_len = (size.height() - 100) // 2

        # 绘制 x 轴
        for i in range(-x_len, x_len + 1):
            painter.drawPoint(i + x_0, y_0)

        # 绘制 x 轴箭头
        for i in range(10):
            painter.drawPoint(x_0 + x_len - i, y_0 - i)
        for i in range(10):
            painter.drawPoint(x_0 + x_len - i, y_0 + i)

        # 绘制 y 轴
        for i in range(-y_len, y_len + 1):
            painter.drawPoint(x_0, i + y_0)

        # 绘制 y 轴箭头
        for i in range(10):
            painter.drawPoint(x_0 - i, y_0 - y_len + i)
        for i in range(10):
            painter.drawPoint(x_0 + i, y_0 - y_len + i)

        # 绘制正弦图像
        painter.setPen(QPen(Qt.blue, 2))
        rang = y_len * 50
        for i in range(rang):
            x = x_len * (-1 + 2.0 * i / rang) + size.width() / 2.0
            y = -y_len * math.sin((x - size.width() / 2.0) * math.pi / y_len) + size.height() / 2.0
            painter.drawPoint(int(x), int(y))

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawPoints()
    mainWin.show()
    sys.exit(app.exec_())
