#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/23 16:16
# 文件名称  :  ListView.py
# 开发工具  :  PyCharm

"""
QListView
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.setWindowTitle('ListView 演示')
        self.setMinimumSize(300, 200)

        listView = QListView()
        listModel = QStringListModel()
        listData = ['Python', 'C/C++', 'Java', 'Ruby']

        listModel.setStringList(listData)
        listView.setModel(listModel)
        listView.clicked.connect(self.listViewClicked)

        vlayout = QVBoxLayout()
        vlayout.addWidget(listView)
        self.setLayout(vlayout)

    def listViewClicked(self, item: QModelIndex):
        QMessageBox.information(self, "listView", '您选择了' + item.data())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ListViewDemo()
    mainWin.show()
    sys.exit(app.exec_())
