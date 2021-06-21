#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 17:43
# 文件名称  :  qCheckBoxDemo.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QChechBoxDemo(QWidget):
    def __init__(self):
        super(QChechBoxDemo, self).__init__()
        self.setWindowTitle('QCheckBox 演示')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 默认处于选中状态
        checkBox1 = QCheckBox('香蕉')
        checkBox1.setChecked(True)
        checkBox1.stateChanged.connect(lambda: self.showCheckBoxState(checkBox1))
        layout.addWidget(checkBox1)

        # 默认处于半选中状态
        checkBox2 = QCheckBox('苹果')
        checkBox2.setTristate(True)
        checkBox2.setCheckState(Qt.PartiallyChecked)
        checkBox2.stateChanged.connect(lambda: self.showCheckBoxState(checkBox2))
        layout.addWidget(checkBox2)

        # 默认处于未选中状态
        checkBox3 = QCheckBox('杏仁')
        checkBox3.stateChanged.connect(lambda: self.showCheckBoxState(checkBox3))
        layout.addWidget(checkBox3)

        self.setLayout(layout)

    def showCheckBoxState(self, checkBox):
        boxState = '<' + checkBox.text() + '>' + '\t是否选中：' + str(checkBox.isChecked()) + '\t状态：' + str(
            checkBox.checkState())
        print(boxState)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QChechBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())
