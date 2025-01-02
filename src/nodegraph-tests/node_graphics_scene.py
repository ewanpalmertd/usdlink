from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import QLine
from PyQt6.QtGui import QColor, QPen
import math


class QDMGraphicsScene(QGraphicsScene):
    
    def __init__(self, scene,  parent=None):
        super().__init__(parent)

        self.scene = scene

        # settings
        self.grid_size = 20
        self.grid_squares = 5
        self._color_background = QColor("#303030") 
        self._color_light = QColor("#252525")  # might change this later as its too light
        self._color_dark = QColor("#2c2c2c")
        self._pen_light = QPen(self._color_light)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)
        self._pen_light.setWidth(1)

        self.setBackgroundBrush(self._color_background)

    def setGrScene(self, width, height):
        self.setSceneRect(-width//2, -height//2, width, height)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # create grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))
        first_left = left - (left % self.grid_size)
        first_top = top - (top % self.grid_size)

        # compute all lines to be drawn
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.grid_size):
            if x % (self.grid_size * self.grid_squares) == 0: 
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            if y % (self.grid_size * self.grid_squares) == 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        # draw the lines
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)

        painter.setPen(self._pen_dark)
        painter.drawLines(*lines_dark)
