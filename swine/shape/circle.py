#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import math

import pyglet

from swine import GameObject, Scene
from .polygon import Polygon


class Circle(Polygon):
    def __init__(self, scene, size, segments=3, fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        points = []

        for i in range(segments):
            angle = math.radians(float(i) / segments * 360)

            _x = size * math.cos(angle) + x
            _y = size * math.sin(angle) + y

            points.append(int(_x))
            points.append(int(_y))

        Polygon.__init__(self, scene, fill, segments, x, y, layer, points, colours=colours)
