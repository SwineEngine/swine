#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import GameObject, Scene
from .polygon import Polygon


class Trapezoid(Polygon):
    def __init__(self, scene, width, height, expand, expand_direction="out", fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, int, str, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)

        if expand_direction == "out":
            tl = x
            bl = x + width + expand
            tr = x + width
            br = x + expand
        elif expand_direction == "in":
            tl = x
            bl = x + width - expand
            tr = x + width
            br = x - expand

        points = [tl, y,  # Top left
                  bl, y,  # Bottom left
                  tr, y + height,  # Top right
                  br, y + height]  # Bottom right
        Polygon.__init__(self, scene, fill, 4, x, y, layer, points, colours=colours)
