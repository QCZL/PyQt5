#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 15:55
# 文件名称  :  InnerHtml.py
# 开发工具  :  PyCharm

"""
显示嵌入式页面
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class InnerHtml(QMainWindow):
    def __init__(self):
        super(InnerHtml, self).__init__()
        self.setWindowTitle('显示嵌入式页面')
        self.resize(1366, 768)

        browser = QWebEngineView()
        browser.setHtml('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>测试页面</title>
        </head>
        <body>
            <h1>Hello PyQt5</h1>
            <h2>Hello PyQt5</h2>
            <h3>Hello PyQt5</h3>
            <h4>Hello PyQt5</h4>
        </body>
        </html>
        ''')
        self.setCentralWidget(browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = InnerHtml()
    mainWin.show()
    sys.exit(app.exec_())
