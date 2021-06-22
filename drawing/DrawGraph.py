#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队  :  Sunniwell
# 开发人员  :  chengc
# 开发时间  :  2021/6/22 9:58
# 文件名称  :  DrawGraph.py
# 开发工具  :  PyCharm


"""
绘制多种图形

1、绘制无弦的弧
painter.drawArc(rect, a, b * 16)

2、绘制带弦的弧
painter.drawChord(rect, a, b * 16)

3、绘制扇形
painter.drawPie(rect, a, b * 16)

    a: 起始角度
    b: 弧度
    rect: 一个范围，图形将被绘制在此范围内，例如：rect = QRect(0, 10, 100, 100)

4、绘制椭圆
point = QPoint(150, 300)
painter.drawEllipse(point, a, b)
    point：原点
    a: 长轴
    b: 短轴

5、绘制多边形
创建对边形对象，坐标需要按顺序传入，否则无法绘制
point = QPoint(x, y)
polygon = QPolygon([point1, point2, point3, point4])
painter.drawPolygon(polygon)

6、绘制图像
image = QImage('../image/liuyifei.jpg')
painter.drawImage(rect, image)

"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawGraph(QWidget):
    def __init__(self):
        super(DrawGraph, self).__init__()
        self.resize(300, 800)
        self.setWindowTitle('绘制多种图形')

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)

        pen = QPen(Qt.blue, 2)
        painter.setPen(pen)
        # 绘制无弦的弧
        rect = QRect(0, 10, 100, 100)   # 设置一个区域，弧将被绘制在此区域内
        painter.drawArc(rect, 30, 45 * 16)

        # 绘制带弦的弧
        painter.drawChord(100, 10, 100, 100, 30, 55 * 16)

        # 通过弦绘制圆
        painter.drawArc(10, 100, 100, 100, 0, 360 * 16)

        # 绘制扇形
        painter.drawPie(100, 100, 100, 100, 10, 75 * 16)

        # 绘制椭圆
        point = QPoint(150, 300)    # 原点
        painter.drawEllipse(point, 100, 75)     # 100：长轴    75 ： 短轴

        # 绘制多边形
        point1 = QPoint(100, 400)
        point2 = QPoint(200, 400)
        point3 = QPoint(200, 500)
        point4 = QPoint(100, 500)
        # 创建对边形对象，坐标需要按顺序传入，否则无法绘制
        polygon = QPolygon([point1, point2, point3, point4])
        painter.drawPolygon(polygon)

        # 绘制图像
        image = QImage('../image/liuyifei.jpg')
        rect = QRect(50, 550, image.width()//2, image.height()//2)
        painter.drawImage(rect, image)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawGraph()
    mainWin.show()
    sys.exit(app.exec_())
