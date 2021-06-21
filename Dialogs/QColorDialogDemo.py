#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 16:38
# 文件名称  :  QColorDialogDemo.py
# 开发工具  :  PyCharm

"""
颜色选择器
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 200)
        self.setWindowTitle('颜色选择器')

        layout = QVBoxLayout()

        button1 = QPushButton('设置字体颜色')
        button1.clicked.connect(self.getFontColor)

        button2 = QPushButton('设置背景颜色')
        button2.clicked.connect(self.getBackgroundColor)

        self.label = QLabel("Hello, 这是测试文本")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def getFontColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)

    def getBackgroundColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QColorDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())
