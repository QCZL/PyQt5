#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 17:28
# 文件名称  :  HBoxLayoutAlign.py
# 开发工具  :  PyCharm

"""
水平盒布局的控件对齐方式
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class HBoxLayoutAlign(QWidget):
    def __init__(self):
        super(HBoxLayoutAlign, self).__init__()
        self.setWindowTitle('水平盒布局')

        layout = QHBoxLayout()
        layout.addWidget(QPushButton('按钮1'), 1, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton('按钮2'), 2, Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(QPushButton('按钮3'), 1, Qt.AlignRight | Qt.AlignBottom)
        layout.addWidget(QPushButton('按钮4'), 3, Qt.AlignCenter)
        layout.addWidget(QPushButton('按钮5'), 2, Qt.AlignRight | Qt.AlignTop)
        # 设置控件间距
        layout.setSpacing(40)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = HBoxLayoutAlign()
    mainWin.show()
    sys.exit(app.exec_())
