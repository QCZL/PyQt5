#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/17 16:44
# 文件名称  :  qLabelDemo.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon, QPixmap
from PyQt5.QtWidgets import *


class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.setUI()

    def setUI(self):
        # 设置坐标系
        # self.setGeometry(400, 300, 600, 400)
        self.resize(600, 400)  # 默认居中

        label_1 = QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)

        label_1.setText("<font color=red>这是一个标签。</font>")
        label_1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(palette.Window, Qt.blue)
        label_1.setPalette(palette)
        label_1.setAlignment(Qt.AlignCenter)

        label_2.setText('<a href="#">这是一个锚点></a>')

        label_3.setText("这是一个图片")
        pixmap = QPixmap('image/7d7c618040004616b9067ec4058b6eaa.jpg')
        label_3.setPixmap(pixmap)
        label_3.setAlignment(Qt.AlignCenter)

        label_4.setOpenExternalLinks(True)
        label_4.setText('<a href="www.jd.com">京东购物</a>')
        label_4.setAlignment(Qt.AlignRight)

        # 鼠标划过的效果
        label_2.linkHovered.connect(self.label_linkHovered)
        # 鼠标点击效果
        label_3.linkActivated.connect(self.label_linkActivated)

        vBox = QVBoxLayout()
        vBox.addWidget(label_1)
        vBox.addWidget(label_2)
        vBox.addWidget(label_3)
        vBox.addWidget(label_4)

        self.setLayout(vBox)
        self.setWindowTitle('QLabel 演示')

    def label_linkHovered(self):
        print('鼠标划过')

    def label_linkActivated(self):
        print('鼠标点击')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qLabelDemo = QLabelDemo()
    qLabelDemo.setWindowIcon(QIcon('icon/Coding.ico'))
    qLabelDemo.show()
    sys.exit(app.exec_())
