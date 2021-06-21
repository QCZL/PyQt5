#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  chengc
# 开发人员  :  chengc
# 开发时间  :  2021/6/19 11:37
# 文件名称  :  qSliderDemo.py
# 开发工具  :  PyCharm

"""
滑块控件
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 400)
        layout = QVBoxLayout()
        self.setWindowTitle('滑块控件演示')

        self.label = QLabel('你好，Python')

        # 竖直方向
        self.slider_v = QSlider(Qt.Vertical)
        # 设置最小值
        self.slider_v.setMinimum(10)
        # 设置最大值
        self.slider_v.setMaximum(30)
        # 设置步长
        self.slider_v.setSingleStep(4)
        # 设置当前值
        self.slider_v.setValue(16)
        # 设置刻度位置，QSlider.TicksBelow 为下方
        self.slider_v.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.slider_v.setTickInterval(2)
        # 事件绑定
        self.slider_v.valueChanged.connect(self.sliderValueChange)

        # 水平方向
        self.slider_h = QSlider(Qt.Horizontal)
        # 设置最小值
        self.slider_h.setMinimum(10)
        # 设置最大值
        self.slider_h.setMaximum(30)
        # 设置步长
        self.slider_h.setSingleStep(4)
        # 设置当前值
        self.slider_h.setValue(16)
        # 设置刻度位置，QSlider.TicksBelow 为下方
        self.slider_h.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.slider_h.setTickInterval(2)
        # 事件绑定
        self.slider_h.valueChanged.connect(self.sliderValueChange)

        layout.addWidget(self.label)
        layout.addWidget(self.slider_h)
        layout.addWidget(self.slider_v)
        self.setLayout(layout)

    def sliderValueChange(self):
        size = self.sender().value()
        self.label.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QSliderDemo()
    mainWin.show()
    sys.exit(app.exec_())
