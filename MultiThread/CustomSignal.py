#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 17:09
# 文件名称  :  CustomSignal.py
# 开发工具  :  PyCharm

"""
自定义信号实现计数器
"""

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class WorkThread(QThread):
    endSignal = pyqtSignal()
    timerSignal = pyqtSignal()

    def __init__(self):
        super(WorkThread, self).__init__()
        self.flag = True
        self.count = 5

    def setCount(self, count: int):
        self.count = count

    def getCount(self):
        return self.count

    def end(self):
        self.flag = False

    def run(self):
        self.flag = True
        while self.flag:
            self.timerSignal.emit()
            # 休眠 1 秒
            self.sleep(1)
            if self.count == 0 or not self.flag:
                self.endSignal.emit()
                break
            self.count -= 1


class CustomSignal(QWidget):
    def __init__(self):
        super(CustomSignal, self).__init__()
        self.setWindowTitle('定时器演示')
        self.resize(400, 300)

        # 设置布局
        gLayout = QGridLayout()

        self.ledNumber = QLCDNumber()
        gLayout.addWidget(self.ledNumber, 0, 0, 1, 3)

        intValidator = QIntValidator()
        intValidator.setRange(1, 100)
        self.lineEdit = QLineEdit()
        self.lineEdit.setValidator(intValidator)
        gLayout.addWidget(self.lineEdit, 1, 0)

        self.startBtn = QPushButton('开始')
        gLayout.addWidget(self.startBtn, 1, 1)

        self.endBtn = QPushButton('停止')
        self.endBtn.setEnabled(False)
        gLayout.addWidget(self.endBtn, 1, 2)

        # 事件处理
        self.work = WorkThread()
        self.work.endSignal.connect(self.countEnd)
        self.work.timerSignal.connect(self.changeLEDNumber)

        # 按钮事件绑定
        self.endBtn.clicked.connect(self.countEnd)
        self.startBtn.clicked.connect(self.countStart)

        self.setLayout(gLayout)

    def countStart(self):
        if self.lineEdit.text() != "":
            self.work.setCount(int(self.lineEdit.text()))
        self.work.start()
        self.endBtn.setEnabled(True)
        self.startBtn.setEnabled(False)
        self.lineEdit.setEnabled(False)

    def countEnd(self):
        self.work.end()
        self.ledNumber.display(0)
        self.endBtn.setEnabled(False)
        self.startBtn.setEnabled(True)
        self.lineEdit.setEnabled(True)

    def changeLEDNumber(self):
        self.ledNumber.display(self.work.getCount())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CustomSignal()
    mainWin.show()
    sys.exit(app.exec_())
