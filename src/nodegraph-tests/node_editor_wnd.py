from PyQt6.QtWidgets import (
    QWidget, QApplication, QGraphicsView, QVBoxLayout, QHBoxLayout, QGraphicsScene, 
    QGraphicsItem, QPushButton, QTextEdit)
from PyQt6.QtGui import QBrush, QPen, QColor
from PyQt6.QtCore import Qt
from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView
from node_scene import Scene
from node_node import Node
import sys


class NodeEditorWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Node Editor")
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()
        # self.gr_scene = self.scene.grScene
        node = Node(self.scene, "TEMPLATE NODE NAME")

        # create graphics view
        self.view = QDMGraphicsView(self.scene.grScene, self)
        # self.view.setScene(self.gr_scene)
        self.layout.addWidget(self.view)

        # self.addDebugContent()
        self.show()

    def addDebugContent(self):
        green_brush = QBrush(Qt.GlobalColor.green)
        outline_pen = QPen(Qt.GlobalColor.black)
        outline_pen.setWidth(2)
        
        rect = self.gr_scene.addRect(-100, -100, 80, 100, outline_pen, green_brush)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        text = self.gr_scene.addText("PLACEHOLDER TEXT")
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))
        
        widget = QPushButton("Push Me")
        proxy = self.gr_scene.addWidget(widget)
        proxy.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        proxy.setPos(0, 30)

        # text editor
        text = QTextEdit()
        proxy_text = self.gr_scene.addWidget(text)
        proxy_text.setPos(30, 50)

        line = self.gr_scene.addLine(-200, -200, 400, -100, outline_pen)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NodeEditorWindow()
    sys.exit(app.exec())
    pass
