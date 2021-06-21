#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 17:51
# 文件名称  :  DrawText.py
# 开发工具  :  PyCharm

"""
绘图 API

绘制流程：
继承 QWidget 并重写 paintEvent 方法
    1. 创建对象
    QPainter
    2. 开始
    QPainter.begin(self)
    3.结束
    QPainter.end()
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo, self).__init__()
        self.setWindowTitle('绘制文本')
        self.resize(400, 300)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.begin(self)

        # 设置画笔颜色
        painter.setPen(QColor(100, 150, 200))
        # 设置字体
        painter.setFont(QFont("微软雅黑", 35))
        # 设置绘制位置和内容
        # event.rect()      可绘制的所有区域
        # Qt.AlignCenter    居中
        painter.drawText(event.rect(), Qt.AlignCenter, '你好，Python')
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawTextDemo()
    mainWin.show()
    sys.exit(app.exec_())
