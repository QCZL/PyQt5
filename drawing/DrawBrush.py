#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 10:47
# 文件名称  :  DrawBrush.py
# 开发工具  :  PyCharm


"""
使用画刷填充区域

Qt.BrushStyle
    SolidPattern = 1
    Dense1Pattern = 2
    Dense2Pattern = 3
    Dense3Pattern = 4
    Dense4Pattern = 5
    Dense5Pattern = 6
    Dense6Pattern = 7
    Dense7Pattern = 8
    HorPattern = 9
    VerPattern = 10
    CrossPattern = 11
    BDiagPattern = 12
    FDiagPattern = 13
    DiagCrossPattern = 14
    LinearGradientPattern = 15
    RadialGradientPattern = 16
    ConicalGradientPattern = 17
    TexturePattern = 24
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawBrush(QWidget):
    def __init__(self):
        super(DrawBrush, self).__init__()
        self.setWindowTitle('使用画刷填充区域')
        self.resize(720, 350)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)

        # Qt.BrushStyle
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 10, 100, 100)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 120, 100, 100)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 230, 100, 100)

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 10, 100, 100)

        brush = QBrush(Qt.Dense4Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 120, 100, 100)

        brush = QBrush(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 230, 100, 100)

        brush = QBrush(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 10, 100, 100)

        brush = QBrush(Qt.Dense7Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 120, 100, 100)

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(250, 230, 100, 100)

        brush = QBrush(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(370, 10, 100, 100)

        brush = QBrush(Qt.CrossPattern)
        painter.setBrush(brush)
        painter.drawRect(370, 120, 100, 100)

        brush = QBrush(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(370, 230, 100, 100)

        brush = QBrush(Qt.FDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(490, 10, 100, 100)

        brush = QBrush(Qt.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(490, 120, 100, 100)

        brush = QBrush(Qt.LinearGradientPattern)
        painter.setBrush(brush)
        painter.drawRect(490, 230, 100, 100)

        brush = QBrush(Qt.RadialGradientPattern)
        painter.setBrush(brush)
        painter.drawRect(610, 10, 100, 100)

        brush = QBrush(Qt.ConicalGradientPattern)
        painter.setBrush(brush)
        painter.drawRect(610, 120, 100, 100)

        brush = QBrush(Qt.TexturePattern)
        painter.setBrush(brush)
        painter.drawRect(610, 230, 100, 100)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawBrush()
    mainWin.show()
    sys.exit(app.exec_())
