#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene
from .polygon import Polygon


class Triangle(Polygon):
    def __init__(self, scene, width, height, fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        points = [x, y, x + width, y,
                  x + (width // 2), y + height]
        Polygon.__init__(self, scene, fill, 3, x, y, layer, points, colours=colours)
