#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import math

import pyglet
import pymunk

from swine import PhysicsObject, Scene


class PhysicsSprite(PhysicsObject, pyglet.sprite.Sprite):
    def __init__(self, scene, image, scale=1, mass=1, friction=0, position=pymunk.Vec2d(0, 50), angle=0, static=False, rotation=True, layer=0):
        # type: (Scene, pyglet.image.AbstractImage) -> None
        self.layer = layer
        pyglet.sprite.Sprite.__init__(self, img=image, batch=scene.batch, group=scene.layers[self.layer])
        PhysicsObject.__init__(self, scene, mass, friction, position, angle, [(-(self.width / 2) * scale, (self.height / 2)), ((self.width / 2) * scale, (self.height / 2)), ((self.width / 2) * scale, -(self.height / 2) * scale), (-(self.width / 2) * scale, -(self.height / 2) * scale)], static, rotation, layer)
        self.scene = scene
        self.image = image
        self.scale = scale

    def physics_update(self, dt=None):
        self.rotation = math.degrees(-self.body.angle)
        self.position = pymunk.Vec2d(self.body.position.x, self.body.position.y)
