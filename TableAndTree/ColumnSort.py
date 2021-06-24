#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 14:57
# 文件名称  :  ColumnSort.py
# 开发工具  :  PyCharm

"""
按照某一列数据排序
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ColumnSortDemo(QWidget):
    def __init__(self):
        super(ColumnSortDemo, self).__init__()
        self.setWindowTitle('数据排序')
        self.resize(400, 200)

        self.sortType = Qt.AscendingOrder
        self.tableWidget = QTableWidget(4, 3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）'])

        listData = [['刘亦菲', '女', '45'],
                    ['刘诗诗', '女', '44'],
                    ['迪丽热巴', '女', '50'],
                    ['古力娜扎', '女', '48']]

        for i in range(len(listData)):
            for j in range(len(listData[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(listData[i][j]))

        sortButton = QPushButton('按体重排序')
        sortButton.clicked.connect(self.sortTable)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(sortButton)
        self.setLayout(layout)

    def sortTable(self):
        if self.sortType == Qt.AscendingOrder:
            self.sortType = Qt.DescendingOrder
        else:
            self.sortType = Qt.AscendingOrder

        self.tableWidget.sortItems(2, self.sortType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ColumnSortDemo()
    mainWin.show()
    sys.exit(app.exec_())
