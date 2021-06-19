#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 17:21
# 文件名称  :  qRadioButtonDemo.py
# 开发工具  :  PyCharm

"""
单选框
"""

import sys
from PyQt5.QtWidgets import *


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.setWindowTitle('QRadioButton 演示')
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        radioBtn1 = QRadioButton()
        radioBtn1.setText('苹果')
        # 设置默认被选中
        radioBtn1.setChecked(True)
        radioBtn1.toggled.connect(self.radioButtonState)
        layout.addWidget(radioBtn1)

        radioBtn2 = QRadioButton()
        radioBtn2.setText('香蕉')
        radioBtn2.toggled.connect(self.radioButtonState)
        layout.addWidget(radioBtn2)

        self.setLayout(layout)

    def radioButtonState(self):
        button = self.sender()
        if button.isChecked():
            print('<', button.text(), '> 被选中')
        else:
            print('<', button.text(), '> 被取消')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QRadioButtonDemo()
    mainWin.show()
    sys.exit(app.exec_())
