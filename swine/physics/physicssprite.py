#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import math

# import pyglet
import rabbyt
import pymunk

from swine import Scene, Sprite
from swine.physics import PhysicsObject


class PhysicsSprite(PhysicsObject, Sprite):  # , pyglet.sprite.Sprite):
    def __init__(self, scene, frames=[], begin=None, fps=None, x=0, y=0, scale=1, mass=1, friction=0, angle=0, vertices=[], static=False, rotation=True, layer=0):
        # type: (Scene, dict) -> None
        self.layer = layer
        # pyglet.sprite.Sprite.__init__(self, img=image, batch=scene.batch, group=scene.layers[self.layer])
        Sprite.__init__(self, scene, frames, begin, fps, scale, layer)

        if not vertices:
            # vertices = [(-(self.width / 2) * scale, (self.height / 2)), ((self.width / 2) * scale, (self.height / 2)), ((self.width / 2) * scale, -(self.height / 2) * scale), (-(self.width / 2) * scale, -(self.height / 2) * scale)]
            vertices = [(-(self.sprite.texture.width / 2) * scale, (self.sprite.texture.height / 2)), ((self.sprite.texture.width / 2) * scale, (self.sprite.texture.height / 2)), ((self.sprite.texture.width / 2) * scale, -(self.sprite.texture.height / 2) * scale), (-(self.sprite.texture.width / 2) * scale, -(self.sprite.texture.height / 2) * scale)]
        PhysicsObject.__init__(self, scene, x, y, mass, friction, angle, vertices, static, rotation, layer)

    def physics_update(self, dt=None):
        self.sprite.rot = math.degrees(self.body.angle)
        self.sprite.xy = self.body.position.x, self.body.position.y
