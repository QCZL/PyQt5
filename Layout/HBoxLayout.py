#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 17:09
# 文件名称  :  HBoxLayout.py
# 开发工具  :  PyCharm

"""
水平盒布局
"""

import sys
from PyQt5.QtWidgets import *


class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout, self).__init__()
        self.setWindowTitle('水平盒布局')

        layout = QHBoxLayout()
        layout.addWidget(QPushButton('按钮1'))
        layout.addWidget(QPushButton('按钮2'))
        layout.addWidget(QPushButton('按钮3'))
        layout.addWidget(QPushButton('按钮4'))
        layout.addWidget(QPushButton('按钮5'))
        # 设置控件间距
        layout.setSpacing(40)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = HBoxLayout()
    mainWin.show()
    sys.exit(app.exec_())
