#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 17:04
# 文件名称  :  AbsoluteLayout.py
# 开发工具  :  PyCharm


"""
绝对布局
"""

import sys
from PyQt5.QtWidgets import *


class AbsoluteLayout(QWidget):
    def __init__(self):
        super(AbsoluteLayout, self).__init__()
        self.setWindowTitle('PyQtCallJS')

        label1 = QLabel('欢迎', self)
        label2 = QLabel('学习', self)
        label3 = QLabel('PyQt5', self)

        label1.move(20, 20)
        label2.move(40, 40)
        label3.move(60, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = AbsoluteLayout()
    mainWin.show()
    sys.exit(app.exec_())
