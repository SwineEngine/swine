#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import GameObject, Scene
from .polygon import Polygon


class Triangle(Polygon):
    def __init__(self, scene, width, height, tip_placement="center", fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, str, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)

        if tip_placement == "center":
            tip = (width // 2)
        elif tip_placement == "left":
            tip = 0
        elif tip_placement == "right":
            tip = width

        points = [x, y,  # Bottom left
                  x + width, y,  # Bottom right
                  x + tip, y + height]  # Tip
        Polygon.__init__(self, scene, fill, 3, x, y, layer, points, colours=colours)
