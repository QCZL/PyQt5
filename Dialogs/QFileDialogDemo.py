#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/21 17:06
# 文件名称  :  QFileDialogDemo.py
# 开发工具  :  PyCharm

"""
文件对话框
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.setWindowTitle('文件选择框演示')

        layout = QVBoxLayout()

        imageButton = QPushButton('请选择图片')
        imageButton.clicked.connect(self.loadImage)
        layout.addWidget(imageButton)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        fileButton = QPushButton("请选择文件")
        fileButton.clicked.connect(self.loadFile)
        layout.addWidget(fileButton)

        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

    def loadImage(self):
        path, ok = QFileDialog.getOpenFileName(self, '打开文件', '.', '图片(*.jpg *.png)')
        if ok:
            self.imageLabel.setPixmap(QPixmap(path))

    def loadFile(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setFilter(QDir.Files)

        if fileDialog.exec():
            fileNames = fileDialog.selectedFiles()
            print(fileNames)

            with open(fileNames[0], encoding='utf-8', mode='r') as f:
                self.textEdit.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QFileDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())
