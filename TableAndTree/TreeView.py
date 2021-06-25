#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 10:32
# 文件名称  :  TreeView.py
# 开发工具  :  PyCharm

"""
treeView
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TreeViewDemo(QWidget):
    def __init__(self):
        super(TreeViewDemo, self).__init__()
        self.setWindowTitle('Tree View')
        self.resize(600, 400)

        model = QDirModel()
        treeView = QTreeView()
        treeView.setModel(model)

        layout = QVBoxLayout()
        layout.addWidget(treeView)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TreeViewDemo()
    mainWin.show()
    sys.exit(app.exec_())
