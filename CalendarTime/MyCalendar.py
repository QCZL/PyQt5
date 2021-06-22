#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 16:43
# 文件名称  :  MyCalendar.py
# 开发工具  :  PyCharm

"""
日历控件
QCalendarWidget
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(300, 300)
        self.setWindowTitle('日历')

        self.calendar = QCalendarWidget(self)
        # 设置最小日期
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        # 设置最大日期
        self.calendar.setMaximumDate(QDate(2099, 12, 31))
        # 显示分割线
        self.calendar.setGridVisible(True)
        self.calendar.move(20, 20)
        # 绑定事件
        self.calendar.clicked.connect(self.showDate)

        self.label = QLabel(self)
        self.label.setText(self.calendar.selectedDate().toString('yyyy-MM-dd dddd'))
        self.label.move(20, 260)

    def showDate(self, date: QDate):
        self.label.setText(date.toString('yyyy-MM-dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyCalendar()
    mainWin.show()
    sys.exit(app.exec_())
