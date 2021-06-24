#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 15:40
# 文件名称  :  CellSize.py
# 开发工具  :  PyCharm

"""
设置单元格的宽和高
# 设置行高
self.tableWidget.setRowHeight(0, 80)
# 设置列宽
self.tableWidget.setColumnWidth(1, 30)
"""

import sys
from PyQt5.QtWidgets import *


class CellSizeDemo(QWidget):
    def __init__(self):
        super(CellSizeDemo, self).__init__()
        self.setWindowTitle('设置单元格的宽和高')
        self.resize(400, 400)

        self.tableWidget = QTableWidget(4, 3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）'])

        # 设置行高
        self.tableWidget.setRowHeight(0, 80)
        # 设置列宽
        self.tableWidget.setColumnWidth(1, 30)

        listData = [['刘亦菲', '女', '45'],
                    ['刘诗诗', '女', '44'],
                    ['迪丽热巴', '女', '50'],
                    ['古力娜扎', '女', '48']]

        for i in range(len(listData)):
            for j in range(len(listData[i])):
                item = QTableWidgetItem(listData[i][j])
                self.tableWidget.setItem(i, j, item)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellSizeDemo()
    mainWin.show()
    sys.exit(app.exec_())
