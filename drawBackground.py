
import math
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtCore import QLine


class GraphicScene(QGraphicsScene):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.nodes = []  # 存储图元
        self.edges = []  # 存储连线
        # 一些关于网格背景的设置
        self.grid_size = 20  # 一块网格的大小 （正方形的）
        self.grid_squares = 5  # 网格中正方形的区域个数

        # 一些颜色
        self._color_background = QColor('#393939')
        self._color_light = QColor('#2f2f2f')
        self._color_dark = QColor('#292929')
        # 一些画笔
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        # 设置画背景的画笔
        self.setBackgroundBrush(self._color_background)
        self.setSceneRect(0, 0, 500, 500)

    # override
    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # 获取背景矩形的上下左右的长度，分别向上或向下取整数
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        # 从左边和上边开始
        first_left = left - (left % self.grid_size)  # 减去余数，保证可以被网格大小整除
        first_top = top - (top % self.grid_size)

        # 分别收集明、暗线
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.grid_size):
            if x % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            if y % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

            # 最后把收集的明、暗线分别画出来
        painter.setPen(self._pen_light)
        if lines_light:
            painter.drawLines(*lines_light)

        painter.setPen(self._pen_dark)
        if lines_dark:
            painter.drawLines(*lines_dark)

    def add_node(self, node):
        self.nodes.append(node)
        self.addItem(node)

    def remove_node(self, node):
        self.nodes.remove(node)
        self.removeItem(node)

    def add_edge(self, edge):
        self.edges.append(edge)
        self.addItem(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)
        self.removeItem(edge)