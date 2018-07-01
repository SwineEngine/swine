#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

# import pyglet

import rabbyt

from swine import GameObject
from swine import Scene


class Sprite(GameObject):  #, pyglet.sprite.Sprite):
    def __init__(self, scene, image, scale=1, layer=0):
        # type: (Scene, str) -> None
        GameObject.__init__(self, scene)
        self.layer = layer
        # pyglet.sprite.Sprite.__init__(self, img=image, batch=scene.batch, group=scene.layers[self.layer])
        self.scene = scene
        self.image = image
        self.scale = scale

        self.sprite = rabbyt.Sprite(rabbyt.pyglet_load_texture(image))
        self.sprite.scale = self.scale

        self.scene.sprite_list.append(self.sprite)
