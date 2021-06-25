#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 16:21
# 文件名称  :  QTimer.py
# 开发工具  :  PyCharm

"""
定时器
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QTimerDemo(QWidget):
    def __init__(self):
        super(QTimerDemo, self).__init__()
        self.setWindowTitle('定时器演示')
        self.resize(400, 300)

        gLayout = QGridLayout()

        # 创建定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        self.label = QLabel('当前时间')
        gLayout.addWidget(self.label, 0, 0, 1, 2)

        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        gLayout.addWidget(self.startBtn, 1, 0)
        gLayout.addWidget(self.endBtn, 1, 1)

        self.endBtn.clicked.connect(self.endTimer)
        self.startBtn.clicked.connect(self.startTimer)

        self.setLayout(gLayout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeText = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText('当前时间：' + timeText)

    def endTimer(self):
        self.timer.stop()
        self.endBtn.setEnabled(False)
        self.startBtn.setEnabled(True)

    def startTimer(self):
        self.timer.start(500)
        self.endBtn.setEnabled(True)
        self.startBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QTimerDemo()
    mainWin.show()
    sys.exit(app.exec_())
