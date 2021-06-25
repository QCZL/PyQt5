#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 9:46
# 文件名称  :  ModifyTree.py
# 开发工具  :  PyCharm


"""
树的增 删 改
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ModifyDemo(QWidget):
    def __init__(self):
        super(ModifyDemo, self).__init__()
        self.setWindowTitle('树的增 删 改')
        self.resize(600, 400)

        self.treeWidget = QTreeWidget()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setHeaderLabels(['参数', '参数值'])

        self.rootWidget = QTreeWidgetItem(self.treeWidget)
        self.rootWidget.setText(0, '根节点')
        for i in range(3):
            parent = QTreeWidgetItem(self.rootWidget)
            parent.setText(0, '测试')
            for j in range(3):
                child = QTreeWidgetItem(parent)
                child.setText(0, '参数')
                child.setText(1, '值')

        addBtn = QPushButton('增加节点')
        updateBtn = QPushButton('更新节点')
        delBtn = QPushButton('删除节点')

        addBtn.clicked.connect(self.addTree)
        updateBtn.clicked.connect(self.updateTree)
        delBtn.clicked.connect(self.delTree)

        hLayout = QHBoxLayout()
        hLayout.addWidget(addBtn)
        hLayout.addWidget(updateBtn)
        hLayout.addWidget(delBtn)

        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.treeWidget)

        self.treeWidget.expandAll()
        self.setLayout(vLayout)

    def addTree(self):
        item = self.treeWidget.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0, '新增节点')
        node.setText(1, '节点值')

    def updateTree(self):
        item = self.treeWidget.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '修改的值')

    def delTree(self):
        item = self.treeWidget.currentItem()
        if item != self.rootWidget:
            item.parent().removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ModifyDemo()
    mainWin.show()
    sys.exit(app.exec_())
