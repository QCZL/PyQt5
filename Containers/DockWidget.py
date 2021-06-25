#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 14:47
# 文件名称  :  DockWidget.py
# 开发工具  :  PyCharm

"""
悬浮窗口
QDockWidget
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo, self).__init__()
        self.setWindowTitle('悬浮窗口')
        self.resize(600, 400)

        listWidget = QListWidget()
        listWidget.addItem('item1')
        listWidget.addItem('item2')
        listWidget.addItem('item3')
        listWidget.addItem('item4')

        self.setCentralWidget(QLineEdit("悬浮窗口"))

        # 创建对象
        dockWidget = QDockWidget()
        # 添加内容
        dockWidget.setWidget(listWidget)
        # 设置是否悬浮
        dockWidget.setFloating(True)

        # 在窗口显示
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DockWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())