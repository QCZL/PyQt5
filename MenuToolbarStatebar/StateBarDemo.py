#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/23 11:31
# 文件名称  :  StateBarDemo.py
# 开发工具  :  PyCharm


import sys
from PyQt5.QtWidgets import *


class StateBarDemo(QMainWindow):
    def __init__(self):
        super(StateBarDemo, self).__init__()
        self.setWindowTitle('状态栏演示')
        self.resize(400, 300)

        menu = self.menuBar()
        file = menu.addMenu('文件')
        file.addAction('新建')
        file.addAction('打开')
        file.addAction('保存')
        file.triggered.connect(self.processTrigger)

        self.stateBar = QStatusBar()
        self.setStatusBar(self.stateBar)

    def processTrigger(self, action: QAction):
        self.stateBar.showMessage(action.text() + '被点击了', 3000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = StateBarDemo()
    mainWin.show()
    sys.exit(app.exec_())
