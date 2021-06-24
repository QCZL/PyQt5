#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/24 10:21
# 文件名称  :  PlaceControlCell.py
# 开发工具  :  PyCharm


"""
QTableWidget 中添加控件

setCellWidget   添加控件
setStyleSheet   设置控件样式
"""

import sys
from PyQt5.QtWidgets import *


class PlaceCtrlCell(QWidget):
    def __init__(self):
        super(PlaceCtrlCell, self).__init__()
        self.setWindowTitle('TableWidget 演示')
        self.setMinimumSize(400, 300)

        tableWidget = QTableWidget(4, 3)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '照片'])

        textItem = QTableWidgetItem('刘亦菲')
        tableWidget.setItem(0, 0, textItem)

        comboBoxItem = QComboBox()
        comboBoxItem.addItem('男')
        comboBoxItem.addItem('女')
        # QSS
        comboBoxItem.setStyleSheet('QComboBox{margin:3px};')
        tableWidget.setCellWidget(0, 1, comboBoxItem)

        buttonItem = QPushButton('选择照片')
        buttonItem.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0, 2, buttonItem)

        vlayout = QVBoxLayout()
        vlayout.addWidget(tableWidget)
        self.setLayout(vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PlaceCtrlCell()
    mainWin.show()
    sys.exit(app.exec_())
