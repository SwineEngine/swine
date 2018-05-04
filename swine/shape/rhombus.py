#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import GameObject, Scene
from .polygon import Polygon


class Rhombus(Polygon):
    def __init__(self, scene, width, height, fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        points = [x, y + (height // 2),
                  x + (width // 2), y,
                  x + width, y + (height // 2),
                  x + (width // 2), y + height]
        Polygon.__init__(self, scene, fill, 4, x, y, layer, points, colours=colours)
