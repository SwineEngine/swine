#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene
from .polygon import Polygon


class Line(Polygon):
    def __init__(self, scene,  height, thickness=1, x=0, y=0, layer=0, *colours):
        # type: (Scene, int, int, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        points = [x, y, x, y + height]

        for i in range(thickness):
            points.append(x + i)
            points.append(y)
            points.append(x + i)
            points.append(y + height)

        Polygon.__init__(self, scene, False, 2 + (thickness * 2), x, y, layer, points, colours=colours)
