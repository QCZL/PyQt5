#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 15:06
# 文件名称  :  QDialogDemo.py
# 开发工具  :  PyCharm

"""
弹出式对话框
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('对话框')
        self.initUI()

    def initUI(self):
        button = QPushButton('弹出对话框', self)
        button.move(100, 80)
        button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        dialog.resize(200, 200)
        dialog.setWindowTitle('弹出式对话框')
        # 设置对话框模式
        dialog.setWindowModality(Qt.ApplicationModal)

        button = QPushButton('确定', dialog)
        button.move(60, 60)
        button.clicked.connect(dialog.close)

        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())
