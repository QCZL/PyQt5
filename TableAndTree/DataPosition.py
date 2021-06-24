#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 11:30
# 文件名称  :  DataPosition.py
# 开发工具  :  PyCharm

"""
QTableWidget 数据定位
1、查找数据
2、定位到指定行
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DataPositionDemo(QWidget):
    def __init__(self):
        super(DataPositionDemo, self).__init__()
        self.setWindowTitle('数据定位')
        self.setMinimumSize(730, 485)

        self.table_row = 15
        self.table_col = 7
        tableWidget = QTableWidget(self.table_row, self.table_col)
        # 隐藏表头
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.horizontalHeader().setVisible(False)

        for i in range(self.table_row):
            for j in range(self.table_col):
                item = QTableWidgetItem('(%d, %d)' % (i, j))
                tableWidget.setItem(i, j, item)

        find_text = '(10, 5)'
        # 精确查找
        items = tableWidget.findItems(find_text, Qt.MatchExactly)
        for item in items:
            print(item.row(), item.column())
            item.setBackground(QBrush(QColor(255, 0, 0)))
            # 定位到指定行
            tableWidget.verticalScrollBar().setSliderPosition(item.row())

        find_text = '(14,'
        # 模糊查找
        items = tableWidget.findItems(find_text, Qt.MatchStartsWith)
        for item in items:
            print(item.row(), item.column())
            item.setBackground(QBrush(QColor(255, 0, 255)))
            # 定位到指定行
            tableWidget.verticalScrollBar().setSliderPosition(item.row())

        hlayout = QHBoxLayout()
        hlayout.addWidget(tableWidget)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DataPositionDemo()
    mainWin.show()
    sys.exit(app.exec_())
