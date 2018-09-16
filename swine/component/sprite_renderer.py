#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

import pymunk
import pyglet.sprite

from swine.component.physics import RigidBody
from swine.object.component import Component
import swine.graphics


class SpriteRenderer(Component):
    def __init__(self, image: swine.graphics.Sprite, layer, scale: int = 1):
        Component.__init__(self)
        self.image = image
        self.layer = layer
        self.scale = scale

        self.sprite: pyglet.sprite.Sprite = None

    def load(self):
        self.sprite = pyglet.sprite.Sprite(self.image.sprite, batch=self.parent.scene.batch, group=self.layer.group)
        self.sprite.scale = self.scale

    def physics_update(self, dt):
        rigid = self.parent.get_component(RigidBody)

        if rigid is not None:
            body = rigid.body
            self.sprite.rotation = math.degrees(-body.angle)
            self.sprite.position = pymunk.Vec2d(body.position.x, body.position.y)

    def unload(self):
        self.sprite.delete()
