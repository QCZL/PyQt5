#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/23 9:59
# 文件名称  :  ToolbarDemo.py
# 开发工具  :  PyCharm

"""
工具栏
工具栏显示模式
1、默认样式，文字在鼠标悬停时显示
    Qt.ToolButtonFollowStyle
2、文字在图标下方
    Qt.ToolButtonTextUnderIcon
3、文字在图标右侧
    Qt.ToolButtonTextBesideIcon
4、只显示文字
    Qt.ToolButtonTextOnly
5、只显示图标，文字在鼠标悬停时显示
    Qt.ToolButtonIconOnly
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ToolsBarDemo(QMainWindow):
    def __init__(self):
        super(ToolsBarDemo, self).__init__()
        self.setWindowTitle('工具栏演示')
        self.initUI()

    def initUI(self):
        self.resize(400, 300)

        toolBar1 = self.addToolBar("文件")
        new_file = QAction(QIcon('../image/file_new_icon_64px.png'), '新建', self)
        toolBar1.addAction(new_file)

        open_file = QAction(QIcon('../image/file_open_icon_64px.png'), '打开', self)
        toolBar1.addAction(open_file)

        save_file = QAction(QIcon('../image/file_save_icon_64px.png'), '保存', self)
        toolBar1.addAction(save_file)

        # 文字在图标下方
        toolBar1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # 文字在图标右侧
        # toolBar1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 默认样式，文字在鼠标悬停时显示
        # toolBar1.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        # 只显示文字
        # toolBar1.setToolButtonStyle(Qt.ToolButtonTextOnly)

        # 只显示图标，文字在鼠标悬停时显示
        # toolBar1.setToolButtonStyle(Qt.ToolButtonIconOnly)

        # 事件绑定
        toolBar1.actionTriggered.connect(self.toolButtonPressed)

    def toolButtonPressed(self, action: QAction):
        print('您点击了工具栏按钮', action.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ToolsBarDemo()
    mainWin.show()
    sys.exit(app.exec_())
