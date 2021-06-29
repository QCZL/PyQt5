#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/29 16:19
# 文件名称  :  PyQtCallJS.py
# 开发工具  :  PyCharm

"""
PyQt 调用 JavaScript
"""
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class PyQtCallJS(QWidget):
    def __init__(self):
        super(PyQtCallJS, self).__init__()
        self.setWindowTitle('PyQtCallJS')
        self.resize(1366, 768)

        layout = QVBoxLayout()

        self.browser = QWebEngineView()
        url = os.getcwd() + '/PyQtCallJS.html'
        self.browser.load(QUrl.fromLocalFile(url))

        fullNameBtn = QPushButton('设置全名')
        fullNameBtn.clicked.connect(self.setFullName)

        layout.addWidget(self.browser)
        layout.addWidget(fullNameBtn)

        self.setLayout(layout)

    def js_callback(self, result):
        print(result)

    def setFullName(self):
        # 执行页面中指定的 javaScript 函数，并调用回调函数打印函数的返回值
        self.browser.page().runJavaScript('fullname();', self.js_callback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PyQtCallJS()
    mainWin.show()
    sys.exit(app.exec_())
