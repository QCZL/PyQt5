#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 16:25
# 文件名称  :  QFontDialogDemo.py
# 开发工具  :  PyCharm

"""
字体选择框
"""
import sys
from PyQt5.QtWidgets import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体选择器')
        layout = QVBoxLayout()

        button = QPushButton('选择字体')
        button.clicked.connect(self.selectFont)

        self.fontText = QLabel('Hello，这是测试字体')

        layout.addWidget(button)
        layout.addWidget(self.fontText)
        self.setLayout(layout)

    def selectFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontText.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QFontDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())
