#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 16:08
# 文件名称  :  textEditDemo.py
# 开发工具  :  PyCharm

"""
多行文本输入框
"""
import sys
from PyQt5.QtWidgets import *


class QTextEditDemo(QWidget):
    def __init__(self):
        # 创建 QTextEdit
        self.textEdit = QTextEdit()
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.setWindowTitle('TextEdit 控件演示')

        btnText = QPushButton('设置文本')
        btnHtml = QPushButton('设置HTML')
        btnToText = QPushButton('获取文本')
        btnToHtml = QPushButton('获取HTML')

        btnText.clicked.connect(self.onClicked_btnText)
        btnHtml.clicked.connect(self.onClicked_btnHtml)
        btnToText.clicked.connect(self.onClicked_btnToText)
        btnToHtml.clicked.connect(self.onClicked_btnToHtml)

        # 纵向布局
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(btnText)
        layout.addWidget(btnHtml)
        layout.addWidget(btnToText)
        layout.addWidget(btnToHtml)

        self.setLayout(layout)

    def onClicked_btnText(self):
        self.textEdit.setText('Hello PyQt5')

    def onClicked_btnHtml(self):
        self.textEdit.setHtml('<font color="red", size=12>你好，PyQt5</font>')

    def onClicked_btnToText(self):
        print(self.textEdit.toPlainText())

    def onClicked_btnToHtml(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QTextEditDemo()
    mainWin.show()
    sys.exit(app.exec_())
