
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QColor, QPen, QPainter, QPainterPath
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem, QGraphicsPathItem
from PyQt5.QtGui import QPixmap
import transformer

class GraphicView(QGraphicsView):

    def __init__(self, graphic_scene, parent=None):
        super().__init__(parent)

        self.gr_scene = graphic_scene  # 将scene传入此处托管，方便在view中维护
        self.parent = parent
        self.init_ui()
        self.edge_enable = False  # 用来记录目前是否可以画线条
        self.drag_edge = None  # 记录拖拽时的线

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
        # 设置拖拽模式
        self.setDragMode(self.RubberBandDrag)
    def edge_drag_start(self, item):
        self.drag_start_item = item  # 拖拽开始时的图元，此属性可以不在__init__中声明
        self.drag_edge = Edge(self.gr_scene, self.drag_start_item, None)  # 开始拖拽线条，注意到拖拽终点为None


    def edge_drag_end(self, item):
        new_edge = Edge(self.gr_scene, self.drag_start_item, item)  # 拖拽结束
        self.drag_edge.remove()  # 删除拖拽时画的线
        self.drag_edge = None
        new_edge.store()  # 保存最终产生的连接

    def mouseDoubleClickEvent(self, event):

        item = self.get_item_at_click(event)

        if isinstance(item, GraphicItem_trans2):  # 判断点击对象是否为图元的实例

            item.trans_2.show()

        elif isinstance(item, GraphicItem_trans3):  # 判断点击对象是否为图元的实例

            item.trans_3.show()

        elif isinstance(item, GraphicItem_wire):  # 判断点击对象是否为图元的实例

            item.wire.show()

        elif isinstance(item, GraphicItem_node):  # 判断点击对象是否为图元的实例

            item.node.show()

        elif isinstance(item, GraphicItem_loader):  # 判断点击对象是否为图元的实例
            item.load.show()

        elif isinstance(item,GraphicItem_gene):
            item.gene.show()

    def get_item_at_click(self, event):
        """ 获取点击位置的图元，无则返回None. """
        pos = event.pos()
        item = self.itemAt(pos)
        return item

    def keyPressEvent(self, event):
        # 当按下键盘E键时，启动线条功能，再次按下则是关闭
        if event.key() == Qt.Key_W:
            self.edge_enable = ~self.edge_enable

    # 此时重构这个方法
    # override
    def mousePressEvent(self, event):
        item = self.get_item_at_click(event)
        if event.button() == Qt.RightButton:
            if isinstance(item, (GraphicItem_trans2,GraphicItem_loader,GraphicItem_trans3,GraphicItem_node,GraphicItem_wire,GraphicItem_gene)):
                item.setTransformOriginPoint(item.boundingRect().center().x(),item.boundingRect().center().y())
                item.setRotation(item.rotation()+90)

        elif self.edge_enable:
            if isinstance(item, (GraphicItem_trans2,GraphicItem_loader,GraphicItem_trans3,GraphicItem_node,GraphicItem_wire,GraphicItem_gene)):
                # 确认起点是图元后，开始拖拽
                self.edge_drag_start(item)

        else:
            # 如果写到最开头，则线条拖拽功能会不起作用
            super().mousePressEvent(event)

    # override
    def mouseReleaseEvent(self, event):
        if self.edge_enable:
            # 拖拽结束后，关闭此功能
            self.edge_enable = False

            item = self.get_item_at_click(event)
            # 终点图元不能是起点图元，即无环图
            if isinstance(item, (GraphicItem_trans2,GraphicItem_loader,GraphicItem_trans3,GraphicItem_node,GraphicItem_wire,GraphicItem_gene)) and item is not self.drag_start_item:
                self.edge_drag_end(item)

            else:
                self.drag_edge.remove()
                self.drag_edge = None
        else:
            super().mouseReleaseEvent(event)

    # override
    def mouseMoveEvent(self, event):
        # 实时更新线条

        pos = event.pos()

        if self.edge_enable and self.drag_edge is not None:

            sc_pos = self.mapToScene(self.mapFromParent(pos))#坐标转换
            self.drag_edge.gr_edge.set_dst(sc_pos.x(), sc_pos.y())
            self.drag_edge.gr_edge.update()
        super().mouseMoveEvent(event)


class GraphicItem_trans2(QGraphicsPixmapItem):
    def __init__(self, address, parent=None):
        super().__init__(parent)
        self.left_node_index = 0
        self.right_node_index = 0
        self.pix = QPixmap(address)
        self.width = 256    # 图元宽
        self.height = 128   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)     # ***设置图元是可以被移动的
        self.trans_2 = transformer.Transformer_Two()

class GraphicItem_trans3(QGraphicsPixmapItem):
    def __init__(self, address, parent=None):
        super().__init__(parent)
        self.left_node_index = 0
        self.right_node_index = 0
        self.down_node_index = 0
        self.pix = QPixmap(address)
        self.width = 512    # 图元宽
        self.height = 256   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)     # ***设置图元是可以被移动的
        self.trans_3 = transformer.Transformer_Three()

class GraphicItem_wire(QGraphicsPixmapItem):
    def __init__(self, address, parent=None):
        super().__init__(parent)
        self.left_node_index = 0
        self.right_node_index = 0
        self.pix = QPixmap(address)
        self.width = 256    # 图元宽
        self.height = 128   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)     # ***设置图元是可以被移动的
        self.wire = transformer.Wire()

class GraphicItem_loader(QGraphicsPixmapItem):
    def __init__(self, address, parent=None):
        super().__init__(parent)
        self.left_node_index = 0
        self.right_node_index = 0
        self.pix = QPixmap(address)
        self.width = 64    # 图元宽
        self.height = 64   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)     # ***设置图元是可以被移动的
        self.load = transformer.Loader()

class GraphicItem_gene(QGraphicsPixmapItem):
    def __init__(self, address, parent=None):
        super().__init__(parent)
        self.left_node_index = 0
        self.right_node_index = 0
        self.pix = QPixmap(address)
        self.width = 64    # 图元宽
        self.height = 64   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)     # ***设置图元是可以被移动的
        self.gene = transformer.Gene()

class GraphicItem_node(QGraphicsPixmapItem):
    def __init__(self, address, parent=None):
        super().__init__(parent)
        self.pix = QPixmap(address)
        self.width = 64    # 图元宽
        self.height = 64   # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)     # ***设置图元是可以被移动的
        self.node = transformer.Node()

















class GraphicEdge(QGraphicsPathItem):
    def __init__(self, edge_wrap, parent=None):
        super().__init__(parent)
        # 这个参数是GraphicEdge的包装类，见下文
        self.edge_wrap = edge_wrap
        self.width = 3.0  # 线条的宽度
        self.pos_src = [0, 0]  # 线条起始位置 x，y坐标
        self.pos_dst = [0, 0]  # 线条结束位置

        self._pen = QPen(QColor(255, 0, 0, 127))  # 画线条的
        self._pen.setWidthF(self.width)

        self._pen_dragging = QPen(QColor("#000"))  # 画拖拽线条时线条的
        self._pen_dragging.setStyle(Qt.DashDotLine)
        self._pen_dragging.setWidthF(self.width)

        self.setFlag(QGraphicsItem.ItemIsSelectable)  # 线条可选
        self.setZValue(-1)  # 让线条出现在所有图元的最下层

    def set_src(self, x, y):
        self.pos_src = [x, y]

    def set_dst(self, x, y):
        self.pos_dst = [x, y]

    # 计算线条的路径
    def calc_path(self):
        path = QPainterPath(QPointF(self.pos_src[0], self.pos_src[1]))  # 起点
        path.lineTo(self.pos_dst[0], self.pos_dst[1])  # 终点
        return path

    # override
    def boundingRect(self):
        return self.shape().boundingRect()

    # override
    def shape(self):
        return self.calc_path()

    # override
    def paint(self, painter, graphics_item, widget=None):
        self.setPath(self.calc_path()) # 设置路径
        path = self.path()
        if self.edge_wrap.end_item is None:
            # 包装类中存储了线条开始和结束位置的图元
            # 刚开始拖拽线条时，并没有结束位置的图元，所以是None
            # 这个线条画的是拖拽路径，点线
            painter.setPen(self._pen_dragging)
            painter.drawPath(path)
        else:
            # 这画的才是连接后的线
            painter.setPen(self._pen)
            painter.drawPath(path)

class Edge:
    def __init__(self, scene, start_item, end_item):
        # 参数分别为场景、开始图元、结束图元
        super().__init__()
        self.scene = scene
        self.start_item = start_item
        self.end_item = end_item

        # 线条图形在此处创建
        self.gr_edge = GraphicEdge(self)
        # 此类一旦被初始化就在添加进scene
        self.scene.add_edge(self.gr_edge)

        # 开始更新
        if self.start_item is not None:
            self.update_positions()

    # 最终保存进scene
    def store(self):
        self.scene.add_edge(self.gr_edge)

    # 更新位置
    def update_positions(self):
        # src_pos 记录的是开始图元的位置，此位置为图元的左上角
        src_pos = self.start_item.pos()
        # 想让线条从图元的中心位置开始，让他们都加上偏移
        patch11 = self.start_item.width / 2
        patch12 = self.start_item.height /2
        self.gr_edge.set_src(src_pos.x()+patch11, src_pos.y()+patch12)
        # 如果结束位置图元也存在，则做同样操作
        if self.end_item is not None:
            if isinstance(self.start_item, GraphicItem_node):
                self.end_item.left_node_index = self.start_item.node.index
            elif isinstance(self.end_item, GraphicItem_node):
                if isinstance(self.start_item, GraphicItem_trans3):
                    if abs(self.start_item.pos().y()-self.end_item.pos().y())>=100 :
                        self.start_item.down_node_index = self.end_item.node.index
                    else:
                        self.start_item.right_node_index = self.end_item.node.index
                else:
                    self.start_item.right_node_index =self.end_item.node.index

            patch21 = self.end_item.width /2
            patch22 = self.end_item.height /2
            end_pos = self.end_item.pos()
            self.gr_edge.set_dst(end_pos.x()+patch21, end_pos.y()+patch22)
        else:
            self.gr_edge.set_dst(src_pos.x()+patch11, src_pos.y()+patch12)
        self.gr_edge.update()

    def remove_from_current_items(self):
        self.end_item = None
        self.start_item = None

    # 移除线条
    def remove(self):
        self.remove_from_current_items()
        self.scene.remove_edge(self.gr_edge)
        self.gr_edge = None


