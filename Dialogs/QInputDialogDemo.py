#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 16:02
# 文件名称  :  QInputDialogDemo.py
# 开发工具  :  PyCharm

"""
输入消息对话框
QInputDialog.getInt     整数输入对话框
QInputDialog.getItem    下拉输入对话框
QInputDialog.getText    文本输入对话框
"""

import sys
from PyQt5.QtWidgets import *


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 400)
        self.setWindowTitle('输入消息对话框')

        formLayout = QFormLayout()

        button1 = QPushButton('下拉选择框', self)
        button1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        formLayout.addRow(self.lineEdit1, button1)

        button2 = QPushButton('整数选择框', self)
        button2.clicked.connect(self.getInt)
        self.lineEdit2 = QLineEdit()
        formLayout.addRow(self.lineEdit2, button2)

        button3 = QPushButton('文本输入框', self)
        button3.clicked.connect(self.getText)
        self.lineEdit3 = QLineEdit()
        formLayout.addRow(self.lineEdit3, button3)

        self.setLayout(formLayout)

    def getItem(self):
        items = ('C', 'C++', 'Ruby', 'Python', 'Java')
        item, ok = QInputDialog.getItem(self, "请选择编程语言", "语言列表", items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "整数输入框", "输入数字")
        if ok:
            self.lineEdit2.setText(str(num))

    def getText(self):
        text, ok = QInputDialog.getText(self, "文本输入框", "输入文本")
        if ok and text:
            self.lineEdit3.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QInputDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())
