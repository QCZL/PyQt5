#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 14:43
# 文件名称  :  CellFontAndColor.py
# 开发工具  :  PyCharm

"""
设置单元格的字体和颜色
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class FontAndColorDemo(QWidget):
    def __init__(self):
        super(FontAndColorDemo, self).__init__()
        self.setWindowTitle('设置字体和颜色')
        self.resize(400, 200)

        tableWidget = QTableWidget(4, 3)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）'])

        item = QTableWidgetItem('刘亦菲')
        # 设置背景色
        item.setBackground(QBrush(QColor(255, 0, 0)))
        # 设置字体
        item.setFont(QFont('Times', 16, QFont.Black))
        tableWidget.setItem(0, 0, item)

        item = QTableWidgetItem('女')
        # 设置前景色
        item.setForeground(QBrush(QColor(0, 255, 255)))
        # 设置字体
        item.setFont(QFont('Times', 16, QFont.Black))
        tableWidget.setItem(0, 1, item)

        item = QTableWidgetItem('45')
        # 设置前景色
        item.setForeground(QBrush(QColor(255, 0, 255)))
        # 设置字体
        item.setFont(QFont('Times', 18, QFont.Black))
        tableWidget.setItem(0, 2, item)

        hlayout = QHBoxLayout()
        hlayout.addWidget(tableWidget)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = FontAndColorDemo()
    mainWin.show()
    sys.exit(app.exec_())
