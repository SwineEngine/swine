#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import GameObject, Scene
from .ellipse import Ellipse


class Circle(Ellipse):
    def __init__(self, scene, size, segments=3, fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, int, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        Ellipse.__init__(self, scene, size, size, segments, fill, x, y, layer, colours=colours)
