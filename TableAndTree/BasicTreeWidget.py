#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 17:26
# 文件名称  :  BasicTreeWidget.py
# 开发工具  :  PyCharm

"""
树控件
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BasicTreeWidgetDemo(QWidget):
    def __init__(self):
        super(BasicTreeWidgetDemo, self).__init__()
        self.setWindowTitle('树控件演示')
        self.resize(600, 400)

        treeWidget = QTreeWidget()
        treeWidget.setColumnCount(2)

        # 设置树头部文字
        treeWidget.setHeaderLabels(['索引', '值'])
        # 设置列宽
        treeWidget.setColumnWidth(0, 150)

        # 跟节点
        rootWidget = QTreeWidgetItem(treeWidget)
        rootWidget.setText(0, '跟节点')

        # 添加子节点
        item1 = QTreeWidgetItem(rootWidget)
        item1.setText(0, '索引1')
        item1.setText(1, '值 1')
        item1.setCheckState(1, Qt.Unchecked)

        # 添加子节点
        item2 = QTreeWidgetItem(rootWidget)
        item2.setText(0, '索引2')
        item2.setText(1, '值 2')
        item2.setCheckState(0, Qt.Checked)

        # 添加子节点
        item3 = QTreeWidgetItem(rootWidget)
        item3.setText(0, '索引3')
        item3.setText(1, '值 3')

        # 添加子节点
        item3_1 = QTreeWidgetItem(item3)
        item3_1.setText(0, '索引3_1')
        item3_1.setText(1, '值 3_1')

        # 展开所有节点
        treeWidget.expandAll()

        layout = QVBoxLayout()
        layout.addWidget(treeWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = BasicTreeWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())
