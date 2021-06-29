#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 15:26
# 文件名称  :  WebEngineView.py
# 开发工具  :  PyCharm

"""
打开外部网址演示
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class WebEngineWidgets(QMainWindow):
    def __init__(self):
        super(WebEngineWidgets, self).__init__()
        self.setWindowTitle('打开外部网址')
        self.resize(1366, 768)

        brower = QWebEngineView()
        brower.load(QUrl('https://www.mi.com'))
        self.setCentralWidget(brower)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WebEngineWidgets()
    mainWin.show()
    sys.exit(app.exec_())
