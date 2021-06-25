#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 15:43
# 文件名称  :  ScrollBar.py
# 开发工具  :  PyCharm


"""
滚动条
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ScrollBarDemo(QWidget):
    def __init__(self):
        super(ScrollBarDemo, self).__init__()
        self.setWindowTitle('滚动条应用')
        self.resize(600, 400)

        self.R = 0
        self.G = 0
        self.B = 0

        self.label = QLabel('拖动滚动条改变字体颜色和位置')

        self.R_Bar = QScrollBar()
        self.G_Bar = QScrollBar()
        self.B_Bar = QScrollBar()
        self.positionBar = QScrollBar()

        # 设置最大值
        self.R_Bar.setMaximum(255)
        self.G_Bar.setMaximum(255)
        self.B_Bar.setMaximum(255)
        self.positionBar.setMaximum(255)

        # 设置步长
        self.R_Bar.setSingleStep(1)
        self.G_Bar.setSingleStep(1)
        self.B_Bar.setSingleStep(1)
        self.positionBar.setSingleStep(1)

        # 事件绑定
        self.R_Bar.sliderMoved.connect(self.setTextColor)
        self.G_Bar.sliderMoved.connect(self.setTextColor)
        self.B_Bar.sliderMoved.connect(self.setTextColor)
        self.positionBar.sliderMoved.connect(self.positonMoved)

        # 设置布局
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.label)
        hLayout.addWidget(self.R_Bar)
        hLayout.addWidget(self.G_Bar)
        hLayout.addWidget(self.B_Bar)
        hLayout.addWidget(self.positionBar)

        self.label_x = self.label.pos().x()
        self.label_y = self.label.pos().y()

        self.setLayout(hLayout)

    def setTextColor(self):
        self.R = self.R_Bar.value()
        self.G = self.G_Bar.value()
        self.B = self.B_Bar.value()
        palette = QPalette()
        palette.setColor(QPalette.Foreground, QColor(self.R, self.G, self.B, 255))
        self.label.setPalette(palette)

    def positonMoved(self):
        self.label.move(self.label_x, self.label_y + self.positionBar.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ScrollBarDemo()
    mainWin.show()
    sys.exit(app.exec_())
