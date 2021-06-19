#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/17 14:49
# 文件名称  :  quitApplication.py
# 开发工具  :  PyCharm

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()

        self.resize(400, 300)
        self.setWindowTitle('退出应用程序')
        # 设置窗口提示信息
        self.setToolTip('这是主窗口区')

        # 添加按钮
        self.quitButton = QPushButton('退出应用程序')
        # 设置按钮提示信息
        self.quitButton.setToolTip('点击后将退出程序')
        # 绑定
        self.quitButton.clicked.connect(self.onClickButton)

        # 创建水平布局
        layout = QHBoxLayout()
        # 向布局中添加按钮
        layout.addWidget(self.quitButton)

        # 窗口
        mainFrame = QWidget()
        # 向窗口中添加布局
        mainFrame.setLayout(layout)
        # 显示窗口
        self.setCentralWidget(mainFrame)

    def onClickButton(self):
        # 退出程序
        QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon/Coding.ico'))
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
