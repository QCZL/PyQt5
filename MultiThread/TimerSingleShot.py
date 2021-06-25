#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/25 16:43
# 文件名称  :  TimerSingleShot.py
# 开发工具  :  PyCharm

"""
timer.singleShot
在指定时间间隔后执行某个任务
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Qt.WindowType
    label = QLabel('<font color=red size=100><b>窗口将在5秒后关闭</b></font>')
    label.setWindowFlag(Qt.SplashScreen)
    label.show()
    QTimer.singleShot(5000, app.exit)
    sys.exit(app.exec_())
