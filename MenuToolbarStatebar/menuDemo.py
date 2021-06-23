#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 17:52
# 文件名称  :  menuDemo.py
# 开发工具  :  PyCharm

"""
菜单
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyMenu(QMainWindow):
    def __init__(self):
        super(MyMenu, self).__init__()
        self.setWindowTitle('菜单演示')
        self.resize(300, 200)
        self.initUI()

    def initUI(self):
        # 获取菜单栏
        bar = self.menuBar()

        file = bar.addMenu('文件')
        file.addAction('新建')

        open_ = QAction('打开', self)
        open_.setIcon(QIcon('../icon/Coding.ico'))
        open_.setShortcut('Ctrl + O')
        open_.triggered.connect(self.openfile)
        file.addAction(open_)

        edit = bar.addMenu('编辑')

        copy = edit.addMenu('复制')
        copy.addAction('复制')
        copy.addAction('复制目录')
        copy.addAction('复制为文本')

        edit.addAction('剪切')
        edit.addAction('粘贴')

    def openfile(self):
        print('open file')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyMenu()
    mainWin.show()
    sys.exit(app.exec_())
