#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import math

import pyglet
import pymunk

from swine import Scene
from swine.physics import PhysicsObject


class PhysicsSprite(PhysicsObject, pyglet.sprite.Sprite):
    def __init__(self, scene, image, x=0, y=0, scale=1, mass=1, friction=0, angle=0, collider=True, vertices=[], static=False, rotation=True, layer=0):
        # type: (Scene, pyglet.image.AbstractImage) -> None
        self.layer = layer
        pyglet.sprite.Sprite.__init__(self, img=image, batch=scene.batch, group=scene.layers[self.layer])
        if not vertices:
            vertices = [(-(self.width / 2) * scale, (self.height / 2)), ((self.width / 2) * scale, (self.height / 2)), ((self.width / 2) * scale, -(self.height / 2) * scale), (-(self.width / 2) * scale, -(self.height / 2) * scale)]

        PhysicsObject.__init__(self, scene, x, y, mass, friction, angle, collider, vertices, static, rotation, layer)
        self.scene = scene
        self.image = image
        self.scale = scale

    def physics_update(self, dt=None):
        self.rotation = math.degrees(-self.body.angle)
        self.position = pymunk.Vec2d(self.body.position.x, self.body.position.y)
