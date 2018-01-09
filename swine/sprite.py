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

        self.sprite = pyglet.sprite.Sprite(img=self.image, batch=scene.batch)
        self._scene.object_list.append(self.sprite)
