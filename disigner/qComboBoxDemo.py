# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/19 11:06
# 文件名称  :  qComboBoxDemo.py
# 开发工具  :  PyCharm

"""
下拉框控件
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle('下拉框演示')
        layout = QVBoxLayout()

        self.label = QLabel("请选择您的编程语言")
        self.comboBox = QComboBox()
        self.comboBox.addItem('Python')
        self.comboBox.addItem('C/C++')
        self.comboBox.addItems(['易语言', 'Java', 'Ruby', "Go"])
        self.comboBox.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)

        self.setLayout(layout)

        # 列举所有项
        for count in range(self.comboBox.count()):
            print('item' + str(count) + ' = ' + self.comboBox.itemText(count))

    def selectionChange(self, index):
        self.label.setText(self.comboBox.currentText())
        self.label.adjustSize()
        print('当前选择 index: ' + str(index) + '\t' + self.comboBox.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QComboBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())
