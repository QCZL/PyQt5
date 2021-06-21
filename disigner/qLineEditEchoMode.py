#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 10:38
# 文件名称  :  qLineEditEchoMode.py
# 开发工具  :  PyCharm


import sys
from PyQt5.QtWidgets import *


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('lineEdit 的回显模式')

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwdLineEdit = QLineEdit()
        passwdEchoOnEditLineEdit = QLineEdit()

        # setPlaceholderText
        normalLineEdit.setPlaceholderText('normal')
        noEchoLineEdit.setPlaceholderText('noEcho')
        passwdLineEdit.setPlaceholderText('password')
        passwdEchoOnEditLineEdit.setPlaceholderText('passwdEchoOnMode')

        # setEchoMode
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwdLineEdit.setEchoMode(QLineEdit.Password)
        passwdEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        fromLayout = QFormLayout()
        fromLayout.addRow('normal', normalLineEdit)
        fromLayout.addRow('noEcho', noEchoLineEdit)
        fromLayout.addRow('password', passwdLineEdit)
        fromLayout.addRow('passwordEchoOnEdit', passwdEchoOnEditLineEdit)

        self.setLayout(fromLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLineEditEchoMode()
    mainWin.show()
    sys.exit(app.exec_())
