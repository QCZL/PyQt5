#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 15:10
# 文件名称  :  MultiWindows.py
# 开发工具  :  PyCharm

"""
多窗口显示
QMdiArea
QMdiSubWindow

.tileSubWindows
.cascadeSubWindows
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MultiWindowsDemo(QMainWindow):
    count = 0

    def __init__(self):
        super(MultiWindowsDemo, self).__init__()
        self.setWindowTitle('多窗口显示')
        self.resize(600, 400)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        menu = self.menuBar()
        file = menu.addMenu('文件')
        file.addAction('新建')
        file.addAction('层叠')
        file.addAction('平铺')

        file.triggered.connect(self.windowsAction)

    def windowsAction(self, item: QAction):
        text = item.text()
        if text == '新建':
            MultiWindowsDemo.count += 1
            newWindow = QMdiSubWindow()
            newWindow.setWidget(QTextEdit())
            newWindow.setWindowTitle('窗口' + str(MultiWindowsDemo.count))
            self.mdi.addSubWindow(newWindow)
            newWindow.show()
        elif text == '层叠':
            self.mdi.cascadeSubWindows()
        elif text == '平铺':
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MultiWindowsDemo()
    mainWin.show()
    sys.exit(app.exec_())
