#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene
from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, scene, size, fill=True, x=0, y=0, layer=0, colours=[]):
        # type: (Scene, int, bool, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        Rectangle.__init__(self, scene, size, size, fill, x, y, layer, colours=colours)
