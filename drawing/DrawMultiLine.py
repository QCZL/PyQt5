#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 9:21
# 文件名称  :  DrawMultiLine.py
# 开发工具  :  PyCharm

"""
绘制不同的直线

Qt.DashLine 等长虚线
Qt.DashDotLine 长短虚线
Qt.DashDotDotLine 长短短虚线
Qt.SolidLine 实线
Qt.CustomDashLine 自定义样式
    pen.setDashPattern([1, 4, 3, 6])    线条长度 间隔长度 线条长度 间隔长度

painter.drawLine(30, 40, 300, 40)       起始 X 坐标， 起始 Y 坐标， 长度， 结束 Y 坐标
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle('绘制不同的直线')

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        # 等长虚线 - - - - - -
        pen = QPen(Qt.blue, 2, Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(30, 40, 300, 40)

        # 长短虚线
        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(30, 60, 300, 60)

        # 长短短虚线
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(30, 80, 300, 80)

        # 实线
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(30, 100, 300, 100)

        # 自定义样式
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 3, 6])
        painter.setPen(pen)
        painter.drawLine(30, 120, 300, 120)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawMultiLine()
    mainWin.show()
    sys.exit(app.exec_())
