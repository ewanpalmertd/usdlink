from PyQt6.QtWidgets import (
    QGraphicsItem, QGraphicsTextItem, QStyleOptionGraphicsItem)
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import (
    QFont, QPainterPath, QPen, QColor, QBrush)


class QDMGraphicsNode(QGraphicsItem):
    def __init__(self, node, title="Node Graphics Item", parent = None):
        super().__init__(parent)
        self._title_color = Qt.GlobalColor.white
        self._title_font = QFont("Lato", 10)

        self.width = 180
        self.height = 240
        self.edge_size = 5.0
        self.title_height = 24
        self._padding = 2.0
        
        self._pen_default = QPen(QColor("#7f000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))
        self._brush_title = QBrush(QColor("#FF313131"))
        self._brush_background = QBrush(QColor("#E3212121"))
        
        self.initTitle()
        self.title = title
        
        self.initUI()

    def initUI(self):
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        self.title_item.setPos(self._padding, 0)
        self.title_item.setTextWidth(
            self.width - 2 * self._padding
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)

    def boundingRect(self):
        return QRectF(
            0, 0, 2 * self.edge_size + self.width, 2 * self.edge_size + self.height
        ).normalized()

    def paint(self, painter, QStyleOptionGraphicsItem, widget = None):
        # title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.FillRule.WindingFill)
        path_title.addRoundedRect(
            0, 0, self.width, self.title_height, self.edge_size, self.edge_size
        )
        path_title.addRect(
            0, self.title_height - self.edge_size, self.edge_size, self.edge_size
        )
        path_title.addRect(
            self.width - self.edge_size, self.title_height - self.edge_size, self.edge_size, self.edge_size 
        )
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        # content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.FillRule.WindingFill)
        path_content.addRoundedRect(
            0, self.title_height, self.width, self.height - self.title_height,
            self.edge_size, self.edge_size
        )
        path_content.addRect(
            0, self.title_height, self.edge_size, self.edge_size
        )
        path_content.addRect(
           self.width - self.edge_size, self.title_height, self.edge_size, self.edge_size
        )
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())
        

        # outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(
            0, 0, self.width, self.height, self.edge_size, self.edge_size)
        painter.setPen(
            self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(path_outline.simplified())
