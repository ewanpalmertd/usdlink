import math

from PyQt6.QtCore import QLine
from PyQt6.QtGui import QColor, QPen
from PyQt6.QtWidgets import QGraphicsScene

from _globals import *


class USDLinkGraphicsScene(QGraphicsScene):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(
            -self.scene_width // 2,
            -self.scene_height // 2,
            self.scene_width,
            self.scene_height,
        )

        self.setBackgroundBrush(QColor(GRUVBOX_BLACK))

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
