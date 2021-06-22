#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 17:07
# 文件名称  :  DateTimeEdit.py
# 开发工具  :  PyCharm

"""
各种 DateTimeEdit
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyDateTimeEdit(QWidget):
    def __init__(self):
        super(MyDateTimeEdit, self).__init__()
        self.setWindowTitle('各种日期控件')
        self.initUI()

    def initUI(self):
        self.resize(400, 100)
        vlayout = QVBoxLayout()

        # 不设置初始值
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit1.setMinimumDate(QDate(1990, 1, 1))
        dateTimeEdit1.setMaximumDate(QDate(2099, 12, 31))
        # 设置显示格式
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd dddd")
        dateTimeEdit1.timeChanged.connect(lambda: self.timeChanged(dateTimeEdit1.time()))

        # 设置初始值
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        # 设置显示格式
        dateTimeEdit2.setDisplayFormat("yyyy-MM-dd hh:mm:ss dddd")
        dateTimeEdit2.setMinimumDate(QDate(1990, 1, 1))
        dateTimeEdit2.setMaximumDate(QDate(2099, 12, 31))
        dateTimeEdit2.dateChanged.connect(lambda: self.dateChanged(dateTimeEdit2.date()))
        # 设置显示样式为日历样式
        dateTimeEdit2.setCalendarPopup(True)

        # 日期控件
        dateEdit = QDateEdit()
        dateEdit.setDisplayFormat('yyyy MM dd')
        dateEdit.setDate(QDate.currentDate())
        dateEdit.dateChanged.connect(lambda: self.dateChanged(dateEdit.date()))

        # 时间控件
        timeEdit = QTimeEdit()
        timeEdit.setTime(QTime.currentTime())
        timeEdit.setDisplayFormat('hh:mm:ss')
        timeEdit.timeChanged.connect(lambda: self.timeChanged(timeEdit.time()))

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)
        self.setLayout(vlayout)

    def dateChanged(self, date: QDateTime):
        print('日期更改为 ', date.toString('yyyy-MM-dd'))

    def timeChanged(self, time: QDateTime):
        print('时间更改为 ', time.toString('HH:mm:ss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyDateTimeEdit()
    mainWin.show()
    sys.exit(app.exec_())
