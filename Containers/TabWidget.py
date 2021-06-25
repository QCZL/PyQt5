#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 10:57
# 文件名称  :  TabWidget.py
# 开发工具  :  PyCharm

"""
TabWidget 选项卡
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TabWidgetDemo(QTabWidget):
    def __init__(self):
        super(TabWidgetDemo, self).__init__()
        self.setWindowTitle('选项卡控件演示')
        self.initUI()

    def initUI(self):
        self.resize(400, 300)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, '选项卡1')
        self.addTab(self.tab2, '选项卡2')
        self.addTab(self.tab3, '选项卡3')

        self.initTab1()
        self.initTab2()
        self.initTab3()

    def initTab1(self):
        self.setTabText(0, '基本信息')
        formLayout = QFormLayout()
        formLayout.addRow('姓名', QLineEdit())
        formLayout.addRow('班级', QLineEdit())
        self.tab1.setLayout(formLayout)

    def initTab2(self):
        self.setTabText(1, '详细信息')

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
        genderLauoyt = QHBoxLayout()
        genderLauoyt.addWidget(QRadioButton('男'))
        genderLauoyt.addWidget(QRadioButton('女'))
        formLayout.addRow('性别', genderLauoyt)
        formLayout.addRow('住址', QLineEdit())
        formLayout.addRow('生日', dateTimeEdit)
        formLayout.addRow('政治面貌', comboBox)
        self.tab2.setLayout(formLayout)

    def initTab3(self):
        self.setTabText(2, '成绩')
        formLayout = QFormLayout()
        formLayout.addRow('语文', QLabel('107'))
        formLayout.addRow('数学', QLabel('136'))
        formLayout.addRow('英语', QLabel('89'))
        formLayout.addRow('综合', QLabel('237'))
        self.tab3.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TabWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())
