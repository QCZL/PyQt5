#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/16 17:19
# 文件名称  :  firstWindow.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FistMainWindow(QMainWindow):
    def __init__(self):
        super(FistMainWindow, self).__init__()
        # 设置窗口标题
        self.setWindowTitle('第一个窗口')

        # 设置窗口尺寸
        self.resize(400, 300)

        # 状态栏消息
        self.status = self.statusBar()
        self.status.showMessage('显示5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置窗口图标
    app.setWindowIcon(QIcon('../icon/Coding.ico'))

    mainWindow = FistMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
