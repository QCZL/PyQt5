#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 15:51
# 文件名称  :  CellImageText.py
# 开发工具  :  PyCharm

"""
单元格显示图标
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CellSizeDemo(QWidget):
    def __init__(self):
        super(CellSizeDemo, self).__init__()
        self.setWindowTitle('设置单元格的宽和高')
        self.resize(600, 400)

        self.tableWidget = QTableWidget(4, 4)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）', '图标'])
        self.tableWidget.cellClicked.connect(self.showImage)

        self.listData = [['刘亦菲', '女', '45', '../image/liuyifei.jpg'],
                         ['刘诗诗', '女', '44', '../image/liushishi.jpg'],
                         ['迪丽热巴', '女', '50', '../image/dilireba.jpg'],
                         ['古力娜扎', '女', '48', '../image/gulinazha.jpg']]

        for i in range(len(self.listData)):
            for j in range(len(self.listData[i])):
                if j == 3:
                    item = QTableWidgetItem(QIcon(self.listData[i][j]), self.listData[i][0])
                else:
                    item = QTableWidgetItem(self.listData[i][j])
                self.tableWidget.setItem(i, j, item)

        self.lable = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.lable)
        self.setLayout(layout)

    def showImage(self, i, j):
        if j == 3:
            self.lable.setPixmap(QPixmap(self.listData[i][j]).scaled(320, 180))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellSizeDemo()
    mainWin.show()
    sys.exit(app.exec_())
