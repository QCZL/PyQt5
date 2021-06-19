#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 9:59
# 文件名称  :  qLabelBuddy.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtWidgets import *


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Label 伙伴关系')

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴关系
        nameLabel.setBuddy(nameLineEdit)

        passwdLabel = QLabel('&Password', self)
        passwdLineEdit = QLineEdit()
        # 设置伙伴关系
        passwdLabel.setBuddy(passwdLineEdit)

        btnOK = QPushButton('&OK', self)
        btnCancel = QPushButton('&Cancel', self)

        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwdLabel, 1, 0)
        mainLayout.addWidget(passwdLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLabelBuddy()
    mainWin.show()
    sys.exit(app.exec_())
