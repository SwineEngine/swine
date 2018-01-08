#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject
from swine import Scene


class Sprite(GameObject):
    def __init__(self, scene, image):
        # type: (Scene, pyglet.image.AbstractImage) -> None
        GameObject.__init__(self, scene)
        self._scene = scene
        self.image = image
