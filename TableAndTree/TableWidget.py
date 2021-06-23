#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/23 16:52
# 文件名称  :  TableWidget.py
# 开发工具  :  PyCharm


import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.setWindowTitle('TableWidget 演示')
        self.setMinimumSize(400, 300)

        tableWidget = QTableWidget(4, 3)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '照片'])
        # 隐藏垂直表头
        tableWidget.verticalHeader().setVisible(False)
        # 设置表格列自适应
        # tableWidget.resizeRowsToContents()
        # 设置表格行自适应
        # tableWidget.resizeColumnsToContents()
        # 整行选择
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格分割线是否显示
        tableWidget.setShowGrid(False)

        listData = [['刘亦菲', '女', '../image/liuyifei.png'],
                    ['刘诗诗', '女', '../image/liuyifei.png']]
        for i in range(len(listData)):
            for j in range(len(listData[i])):
                tableWidget.setItem(i, j, QTableWidgetItem(listData[i][j]))

        vlayout = QVBoxLayout()
        vlayout.addWidget(tableWidget)
        self.setLayout(vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TableWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())
