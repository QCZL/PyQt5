#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 15:20
# 文件名称  :  QMessageBoxDemo.py
# 开发工具  :  PyCharm

"""
消息对话框

1. 关于对话框
2. 错误对话框
3. 警告对话框
4. 提问对话框
5. 消息对话框

差异：
1. 对话框图标可能不一样
2. 显示的按钮可能不一样
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 400)
        self.setWindowTitle('消息对话框演示')

        layout = QVBoxLayout()

        # 关于对话框
        button1 = QPushButton('显示关于对话框', self)
        button1.clicked.connect(self.aboutBox)

        # 错误对话框
        button2 = QPushButton('显示错误对话框', self)
        button2.clicked.connect(self.criticalBox)

        # 警告对话框
        button3 = QPushButton('显示警告对话框')
        button3.clicked.connect(self.warningBox)

        # 提问对话框
        button4 = QPushButton('显示提问对话框')
        button4.clicked.connect(self.questionBox)

        # 消息对话框
        button5 = QPushButton('显示消息对话框')
        button5.clicked.connect(self.informationBox)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        self.setLayout(layout)

    def aboutBox(self):
        QMessageBox.about(self, '关于', '这是一个关于对话框')

    def criticalBox(self):
        result = QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if result == QMessageBox.Yes:
            print('您选择了 YES')
        elif result == QMessageBox.No:
            print('您选择了 NO')

    def warningBox(self):
        QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes, QMessageBox.Yes)

    def questionBox(self):
        QMessageBox.question(self, '提问', '这是一个提问对话框')

    def informationBox(self):
        QMessageBox.information(self, '消息', '这是一个消息对话框')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMessageBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())
