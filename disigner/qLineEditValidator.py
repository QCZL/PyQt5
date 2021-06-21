#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 11:02
# 文件名称  :  qLineEditValidator.py
# 开发工具  :  PyCharm


"""
输入校验器
QIntValidator : 整数校验器
QDoubleValidator : 浮点数校验器
QRegExpValidator ： 正则表达式校验器
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValiDator(QWidget):
    def __init__(self):
        super(QLineEditValiDator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入校验器')

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regExpLineEdit = QLineEdit()

        fromLayout = QFormLayout()
        fromLayout.addRow('intValidator', intLineEdit)
        fromLayout.addRow('doubleValidator', doubleLineEdit)
        fromLayout.addRow('regExpValidator', regExpLineEdit)

        # 创建整数校验器
        intValidator = QIntValidator()
        intValidator.setRange(1, 100)  # 设置范围，不咋好用

        # 创建浮点数校验器
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-1000, 1000)  # 设置范围，不咋好用
        doubleValidator.setDecimals(2)  # 设置精度
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)

        # 创建自定义校验器
        reg = QRegExp('[a-zA-Z0-9]+$')
        regExpValidator = QRegExpValidator()
        regExpValidator.setRegExp(reg)

        # 绑定校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regExpLineEdit.setValidator(regExpValidator)

        self.setLayout(fromLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLineEditValiDator()
    mainWin.show()
    sys.exit(app.exec_())
