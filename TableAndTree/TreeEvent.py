#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 17:54
# 文件名称  :  TreeEvent.py
# 开发工具  :  PyCharm

"""
树控件的事件演示
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TerrEventDemo(QWidget):
    def __init__(self):
        super(TerrEventDemo, self).__init__()
        self.setWindowTitle('树控件的事件演示')
        self.resize(600, 400)

        self.treeWidget = QTreeWidget()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setHeaderLabels(['参数', '参数值'])

        listData = [[{'姓名': '刘亦菲'}, {'性别': '女', '体重': 45, '图像': '../image/liuyifei.jpg'}],
                    [{'姓名': '刘诗诗'}, {'性别': '女', '体重': 44, '图像': '../image/liushishi.jpg'}],
                    [{'姓名': '迪丽热巴'}, {'性别': '女', '体重': 50, '图像': '../image/dilireba.jpg'}]]

        rootWidget = QTreeWidgetItem(self.treeWidget)
        rootWidget.setText(0, '所有明星')
        for i in range(len(listData)):
            for key0, value0 in listData[i][0].items():
                child1 = QTreeWidgetItem(rootWidget)
                child1.setText(0, str(value0))
                for key1, value1 in listData[i][1].items():
                    child2 = QTreeWidgetItem(child1)
                    child2.setText(0, str(key1))
                    child2.setText(1, str(value1))
                    if key1 == '图像':
                        child2.setIcon(1, QIcon(value1))

        # 绑定事件
        self.treeWidget.clicked.connect(self.onClickTree)
        self.imageLabel = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.treeWidget)
        layout.addWidget(self.imageLabel)
        self.setLayout(layout)

    def onClickTree(self, index: QModelIndex):
        row = index.row()
        col = index.column()
        if row == 2 and col == 1:
            self.imageLabel.setPixmap(QPixmap(index.data()).scaled(320, 180))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TerrEventDemo()
    mainWin.show()
    sys.exit(app.exec_())
