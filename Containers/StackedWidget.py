#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 14:15
# 文件名称  :  StackedWidget.py
# 开发工具  :  PyCharm

"""
堆栈窗口显示
QStackedWidget
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class StackedWidgetDemo(QWidget):
    def __init__(self):
        super(StackedWidgetDemo, self).__init__()
        self.setWindowTitle('堆栈窗口显示')
        self.initUI()

    def initUI(self):
        self.resize(400, 300)

        self.listWidget = QListWidget()
        self.listWidget.insertItem(0, '基本信息')
        self.listWidget.insertItem(1, '详细信息')
        self.listWidget.insertItem(2, '各科成绩')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.initStack1()
        self.initStack2()
        self.initStack3()

        self.rootStack = QStackedWidget()
        self.rootStack.addWidget(self.stack1)
        self.rootStack.addWidget(self.stack2)
        self.rootStack.addWidget(self.stack3)

        # 事件绑定
        self.listWidget.currentRowChanged.connect(self.displayStack)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.listWidget)
        hLayout.addWidget(self.rootStack)
        self.setLayout(hLayout)

    def initStack1(self):
        formLayout = QFormLayout()
        formLayout.addRow('姓名', QLineEdit())
        formLayout.addRow('班级', QLineEdit())
        self.stack1.setLayout(formLayout)

    def initStack2(self):
        # 设置初始值
        dateTimeEdit = QDateTimeEdit(QDateTime.currentDateTime())
        # 设置显示格式
        dateTimeEdit.setDisplayFormat("yyyy-MM-dd")
        dateTimeEdit.setMinimumDate(QDate(1990, 1, 1))
        dateTimeEdit.setMaximumDate(QDate(2099, 12, 31))
        # 设置显示样式为日历样式
        dateTimeEdit.setCalendarPopup(True)

        comboBox = QComboBox()
        comboBox.addItems(['团员', '党员', '无党派人士'])

        formLayout = QFormLayout()
        genderLayout = QHBoxLayout()
        genderLayout.addWidget(QRadioButton('男'))
        genderLayout.addWidget(QRadioButton('女'))
        formLayout.addRow('性别', genderLayout)
        formLayout.addRow('住址', QLineEdit())
        formLayout.addRow('生日', dateTimeEdit)
        formLayout.addRow('政治面貌', comboBox)
        self.stack2.setLayout(formLayout)

    def initStack3(self):
        formLayout = QFormLayout()
        formLayout.addRow('语文', QLabel('107'))
        formLayout.addRow('数学', QLabel('136'))
        formLayout.addRow('英语', QLabel('89'))
        formLayout.addRow('综合', QLabel('237'))
        self.stack3.setLayout(formLayout)

    def displayStack(self, index):
        self.rootStack.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = StackedWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())
