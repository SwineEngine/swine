#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import GameObject, Scene
from .rectangle import Rectangle


class Line(Rectangle):
    def __init__(self, scene, height, thickness=1, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        Rectangle.__init__(self, scene, thickness, height, True, x, y, layer, colours=colours)
