import math

from PyQt6.QtCore import QLine
from PyQt6.QtGui import QColor, QPen
from PyQt6.QtWidgets import QGraphicsScene

from _globals import *


class USDLinkGraphicsScene(QGraphicsScene):

    def __init__(self, lines: bool = True, parent=None):
        super().__init__(parent)

        self.grid_size: int = 20
        self.grid_chunks: int = 5

        # TODO need a better solution for choosing colors
        # TODO need to add an optional arg for enabling and disabling the grid
        self._color_dark = QColor(GRUVBOX_WHITE)  # temporary solution

        self._pen_light = QPen(QColor(GRUVBOX_MIDGREY))
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(
            -self.scene_width // 2,
            -self.scene_height // 2,
            self.scene_width,
            self.scene_height,
        )

        if lines:
            self.setBackgroundBrush(QColor(GRUVBOX_BLACK))

    def drawBackground(self, painter, rect):
        """
        drawing the grid background

        - need to make the grid optional
        - need to make the grid colours more procedural using args
        """
        super().drawBackground(painter, rect)

        # create the grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.grid_size)
        first_top = top - (top % self.grid_size)

        # compute all lines to be drawn
        lines_light, lines_dark = [], []
        # TODO need a way to disable lines light and lines dark (not prio)
        for x in range(first_left, right, self.grid_size):
            # TODO turn 100 value into a variable for more grid control
            if x % (self.grid_size * self.grid_chunks) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            if y % (self.grid_size * self.grid_chunks) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        # draw the light lines
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)

        # draw the dark lines
        painter.setPen(self._pen_dark)
        painter.drawLines(*lines_dark)
