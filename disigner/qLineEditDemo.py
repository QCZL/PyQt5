#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/18 14:29
# 文件名称  :  qLineEditDemo.py
# 开发工具  :  PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLineEdit 综合实例')

        # 整数校验器
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(6)

        # 掩码校验
        edit2 = QLineEdit()
        edit2.setInputMask('DDDD-DD-DD;_')

        # 正则表达式校验
        edit3 = QLineEdit()
        reg = QRegExp(r'(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))')
        edit3.setValidator(QRegExpValidator(reg))

        # 密码
        edit4 = QLineEdit()
        edit4.setEchoMode(QLineEdit.Password)
        edit4.editingFinished.connect(self.editingPass)

        # 文本bianhua
        edit5 = QLineEdit()
        edit5.textChanged.connect(self.editTextChanged)

        # 只读属性
        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)

        fromLayout = QFormLayout()
        fromLayout.addRow('整数', edit1)
        fromLayout.addRow('日期', edit2)
        fromLayout.addRow('IP 地址', edit3)
        fromLayout.addRow('密码', edit4)
        fromLayout.addRow('文本变化', edit5)
        fromLayout.addRow('只读文本', edit6)

        self.setLayout(fromLayout)

    def editTextChanged(self, text):
        print('文本变化', text)

    def editingPass(self):
        print('输入完成')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLineEditDemo()
    mainWin.show()
    sys.exit(app.exec_())
