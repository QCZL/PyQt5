#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 16:42
# 文件名称  :  qPushButtonDemo.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.setWindowTitle('QPushButton 演示')
        self.resize(300, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 普通按钮
        self.btn1 = QPushButton()
        self.btn1.setText('第 1 个按钮')
        self.btn1.clicked.connect(lambda: self.whichSelect(self.btn1))
        layout.addWidget(self.btn1)

        # 带图标按钮
        self.btn2 = QPushButton()
        self.btn2.setText('第 2 个按钮')
        self.btn2.setIcon(QIcon(QPixmap('icon/Coding.ico')))
        layout.addWidget(self.btn2)

        # 不可用按钮
        self.btn3 = QPushButton('第 3 个按钮')
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)

        # 有热键的按钮
        self.btn4 = QPushButton('&M第 4 个按钮')
        self.btn4.clicked.connect(lambda: self.whichSelect(self.btn4))
        layout.addWidget(self.btn4)

    def whichSelect(self, btn):
        print('按钮<', btn.text(), '>被点击')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QPushButtonDemo()
    mainWin.show()
    sys.exit(app.exec_())
