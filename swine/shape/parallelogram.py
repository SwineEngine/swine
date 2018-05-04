#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene
from .polygon import Polygon


class Parallelogram(Polygon):
    def __init__(self, scene, width, height, skew, skew_direction="right", fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, int, str, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)

        if skew_direction == "left":
            tl = x + skew
            bl = x + width + skew
            tr = x + width - skew
            br = x - skew
        elif skew_direction == "right":
            tl = x - skew
            bl = x + width - skew
            tr = x + width + skew
            br = x + skew

        points = [tl, y, bl, y,
                  tr, y + height, br, y + height]
        Polygon.__init__(self, scene, fill, 4, x, y, layer, points, colours=colours)
