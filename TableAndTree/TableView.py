#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/23 14:35
# 文件名称  :  TableView.py
# 开发工具  :  PyCharm

"""
QTableView 演示
1、创建 QStandardItemModel
    # 设置横向表头
    model.setHorizontalHeaderLabels(['序号', '姓名', '性别'])
    # 设置纵向表头
    model.setVerticalHeaderLabels(['4', '3', '2', '1'])
2、创建 QTableView
3、关联 QStandardItemModel 和 QTableView
    table.setModel(model)
4、添加数据
    model.setItem(x, y, QStandardItem(data))
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.setWindowTitle('tableView 演示')
        self.setMinimumSize(339, 200)
        self.initUI()

    def initUI(self):
        model = QStandardItemModel(4, 3)
        # 设置横向表头
        model.setHorizontalHeaderLabels(['序号', '姓名', '性别'])
        # 设置纵向表头
        # model.setVerticalHeaderLabels(['4', '3', '2', '1'])
        table = QTableView()
        # 关联 table 和 model
        table.setModel(model)

        data = [['000', '刘亦菲', '女'], ['001', '迪丽热巴', '女'], ['002', '刘诗诗', '女']]
        for i in range(len(data)):
            for j in range(len(data[i])):
                model.setItem(i, j, QStandardItem(data[i][j]))

        vlayout = QVBoxLayout()
        vlayout.addWidget(table)
        self.setLayout(vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TableViewDemo()
    mainWin.show()
    sys.exit(app.exec_())
