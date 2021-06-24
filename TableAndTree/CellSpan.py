#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 15:29
# 文件名称  :  CellSpan.py
# 开发工具  :  PyCharm


"""
合并单元格

self.tableWidget.setSpan(row, col, row_n, col_n)
    row     :   起始行
    col     :   起始列
    row_n   :   要合并的行数
    col_n   :   要合并的列数
"""

import sys
from PyQt5.QtWidgets import *


class CellTextAlignmentDemo(QWidget):
    def __init__(self):
        super(CellTextAlignmentDemo, self).__init__()
        self.setWindowTitle('合并单元格')
        self.resize(400, 200)

        self.tableWidget = QTableWidget(4, 3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）'])

        listData = [['刘亦菲', '女', '45'],
                    ['刘诗诗', '女', '44'],
                    ['迪丽热巴', '女', '50'],
                    ['古力娜扎', '女', '48']]

        for i in range(len(listData)):
            for j in range(len(listData[i])):
                item = QTableWidgetItem(listData[i][j])
                self.tableWidget.setItem(i, j, item)

        # 合并单元格
        self.tableWidget.setSpan(0, 1, 4, 1)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellTextAlignmentDemo()
    mainWin.show()
    sys.exit(app.exec_())
