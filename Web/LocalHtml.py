#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 15:49
# 文件名称  :  LocalHtml.py
# 开发工具  :  PyCharm


"""
加载本地页面
"""
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class LocalHtml(QMainWindow):
    def __init__(self):
        super(LocalHtml, self).__init__()
        self.setWindowTitle('打开外部网址')
        self.resize(1366, 768)

        browser = QWebEngineView()
        url = os.getcwd() + '/LocalTest.html'
        browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = LocalHtml()
    mainWin.show()
    sys.exit(app.exec_())