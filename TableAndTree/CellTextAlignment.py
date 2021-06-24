#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 15:13
# 文件名称  :  CellTextAlignment.py
# 开发工具  :  PyCharm


"""
设置单元格文本对齐方式
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class CellTextAlignmentDemo(QWidget):
    def __init__(self):
        super(CellTextAlignmentDemo, self).__init__()
        self.setWindowTitle('数据排序')
        self.resize(400, 200)

        self.tableWidget = QTableWidget(4, 3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）'])

        listData = [['刘亦菲', '女', '45'],
                    ['刘诗诗', '女', '44'],
                    ['迪丽热巴', '女', '50'],
                    ['古力娜扎', '女', '48']]

        for i in range(len(listData)):
            for j in range(len(listData[i])):
                alignment = Qt.AlignTop
                if i == 0:
                    alignment = Qt.AlignRight
                elif i == 1:
                    alignment = Qt.AlignBottom
                elif i == 2:
                    alignment = Qt.AlignHCenter
                item = QTableWidgetItem(listData[i][j])
                item.setTextAlignment(alignment)
                self.tableWidget.setItem(i, j, item)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellTextAlignmentDemo()
    mainWin.show()
    sys.exit(app.exec_())
