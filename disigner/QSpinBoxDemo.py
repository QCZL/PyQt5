#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 14:40
# 文件名称  :  QSpinBoxDemo.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.setWindowTitle('计数器 演示')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.resize(300, 100)

        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)

        self.spinBox = QSpinBox()
        self.spinBox.setRange(100, 500)
        self.spinBox.setSingleStep(5)
        self.spinBox.valueChanged.connect(self.ValueChange)

        layout.addWidget(self.label)
        layout.addWidget(self.spinBox)
        self.setLayout(layout)

    def ValueChange(self):
        self.label.setText('当前值：' + str(self.spinBox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QSpinBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())
