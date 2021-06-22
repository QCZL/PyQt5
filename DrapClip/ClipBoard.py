#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 15:51
# 文件名称  :  ClipBoard.py
# 开发工具  :  PyCharm

"""
使用剪切板

x.addWidget()
第一个参数：需要插入的子布局对象
第二个参数：插入的起始行
第三个参数：插入的起始列
第四个参数：占用的行数
第五个参数：占用的列数
第六个参数：指定的对齐方式
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ClipBoardDemo(QDialog):
    def __init__(self):
        super(ClipBoardDemo, self).__init__()
        self.setWindowTitle('使用剪切板')

        self.clipboard = QApplication.clipboard()

        copyTextButton = QPushButton('复制文本')
        pasteTextButton = QPushButton('粘贴文本')
        copyImageButton = QPushButton('复制图片')
        pasteImageButton = QPushButton('粘贴图片')
        copyHtmlButton = QPushButton('复制Html')
        pasteHtmlButton = QPushButton('粘贴Html')

        self.textEdit = QTextEdit("默认文本")
        self.imageLabel = QLabel("显示图像")
        self.imageLabel.setStyleSheet('border:1px solid black')

        copyTextButton.clicked.connect(self.copyText)
        pasteTextButton.clicked.connect(self.pasteText)
        copyImageButton.clicked.connect(self.copyImage)
        pasteImageButton.clicked.connect(self.pasteImage)
        copyHtmlButton.clicked.connect(self.copyHtml)
        pasteHtmlButton.clicked.connect(self.pasteHtml)

        # 栅格布局
        layout = QGridLayout()
        layout.addWidget(copyTextButton, 0, 0)
        layout.addWidget(pasteTextButton, 0, 1)
        layout.addWidget(copyImageButton, 0, 2)
        layout.addWidget(pasteImageButton, 0, 3)
        layout.addWidget(copyHtmlButton, 0, 4)
        layout.addWidget(pasteHtmlButton, 0, 5)
        layout.addWidget(self.textEdit, 1, 0, 4, 3)
        layout.addWidget(self.imageLabel, 1, 3, 4, 3)
        self.setLayout(layout)

    def copyText(self):
        self.clipboard.setText(self.textEdit.toPlainText())

    def pasteText(self):
        self.textEdit.setText(self.clipboard.text())

    def copyImage(self):
        self.clipboard.setPixmap(QPixmap('../image/liuyifei.jpg'))

    def pasteImage(self):
        self.imageLabel.setPixmap(self.clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>你好，刘亦菲 <font color=blue>你好，程诚</font>')
        self.clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        mimeData = self.clipboard.mimeData()
        if mimeData.hasHtml():
            self.textEdit.setHtml(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ClipBoardDemo()
    mainWin.show()
    sys.exit(app.exec_())
