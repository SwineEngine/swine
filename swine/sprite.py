#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject
from swine import Scene


class Sprite(GameObject):
    def __init__(self, scene, image, scale=1):
        # type: (Scene, pyglet.image.AbstractImage) -> None
        GameObject.__init__(self, scene)
        self._scene = scene
        self.image = image
        self.scale = scale

        self.sprite = pyglet.sprite.Sprite(img=self.image, batch=scene.batch)
        self.sprite.scale = self.scale

        self._scene.object_list.append(self.sprite)
