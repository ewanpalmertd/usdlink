from PyQt6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

from graphics_scene import USDLinkGraphicsScene


class UsdLinkWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self) -> None:
        """initilising interface"""
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("USDLink")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # create graphics scene
        self.graphics_scene = USDLinkGraphicsScene()

        # create graphics view
        self.view = QGraphicsView(self)
        self.view.setScene(self.graphics_scene)
        self.layout.addWidget(self.view)

        self.setLayout(self.layout)
        self.show()
