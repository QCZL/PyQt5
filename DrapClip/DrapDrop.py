#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 11:22
# 文件名称  :  DrapDrop.py
# 开发工具  :  PyCharm


"""
控件拖拽
例如将 A 控件拖拽至 B 控件

A 控件需要：
    1、设置控件可以被拖拽 setDragEnabled

B 控件需要：
    1、重写控件的 dragEnterEvent 方法
    2、重写控件的 dropEvent 方法
    3、设置控件可以接受拖拽 setAcceptDrops
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        # 设置控件支持接受拖拽
        self.setAcceptDrops(True)

    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        if a0.mimeData().hasText():
            a0.accept()
        else:
            a0.ignore()

    def dropEvent(self, a0: QDropEvent) -> None:
        self.addItem(a0.mimeData().text())


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        self.setWindowTitle('控件拖拽')
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        myCombo = MyComboBox()
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)

        layout.addWidget(lineEdit)
        layout.addWidget(myCombo)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrapDropDemo()
    mainWin.show()
    sys.exit(app.exec_())
