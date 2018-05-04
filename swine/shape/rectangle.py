#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import GameObject, Scene
from .polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, scene, width, height, fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        points = [x, y,  # Top left
                  x + width, y,  # Bottom left
                  x + width, y + height,  # Top Right
                  x, y + height]  # Bottom Right
        Polygon.__init__(self, scene, fill, 4, x, y, layer, points, colours=colours)
