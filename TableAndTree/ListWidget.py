#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/23 16:33
# 文件名称  :  ListWidget.py
# 开发工具  :  PyCharm

"""
QListWidget
"""
import sys
from PyQt5.QtWidgets import *


class ListWidgetDemo(QWidget):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle('ListWidget 演示')
        self.setMinimumSize(300, 200)

        self.listWidget = QListWidget()
        self.listWidget.addItem('刘亦菲')
        self.listWidget.addItem('刘诗诗')
        self.listWidget.addItem('迪丽热巴')
        self.listWidget.addItem('古力娜扎')
        self.listWidget.itemClicked.connect(self.itemClicked)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.listWidget)
        self.setLayout(vlayout)

    def itemClicked(self, item: QListWidgetItem):
        QMessageBox.information(self, '您选择了', item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ListWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())
