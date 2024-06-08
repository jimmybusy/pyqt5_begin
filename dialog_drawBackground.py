import math
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QPointF , QPoint
from PyQt5.QtGui import QColor, QPen, QPainter, QPainterPath
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem, QGraphicsPathItem
from PyQt5.QtGui import QPixmap
class GraphicView(QGraphicsView):

    def __init__(self, graphic_scene, parent=None):
        super().__init__(parent)
        self.gr_scene = graphic_scene  # 将scene传入此处托管，方便在view中维护
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setScene(self.gr_scene)
        # 设置渲染属性
        self.setRenderHints(QPainter.Antialiasing |                    # 抗锯齿
                            QPainter.HighQualityAntialiasing |         # 高品质抗锯齿
                            QPainter.TextAntialiasing |                # 文字抗锯齿
                            QPainter.SmoothPixmapTransform |           # 使图元变换更加平滑
                            QPainter.LosslessImageRendering)           # 不失真的图片渲染
        # 视窗更新模式
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        # 设置水平和竖直方向的滚动条不显示
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(self.AnchorUnderMouse)





class Mode_wire(QGraphicsPixmapItem):
    def __init__(self,i, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("./image/model.png")
        self.width = 256    # 图元宽
        self.height = 128   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的

class Mode_trans2(QGraphicsPixmapItem):
    def __init__(self,i, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("./image/model.png")
        self.width = 256    # 图元宽
        self.height = 128   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的


class Mode_trans3(QGraphicsPixmapItem):
    def __init__(self,i, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("./image/model3.png")
        self.width = 512    # 图元宽
        self.height = 256   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的

class Mode_node(QGraphicsPixmapItem):
    def __init__(self,i, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("./image/model_node.png")
        self.width = 256    # 图元宽
        self.height = 128   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的

