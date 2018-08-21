#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

import pymunk

from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.object.component import Component


class Transform(Component):
    def __init__(self, position: pymunk.Vec2d = pymunk.Vec2d(0, 0), rotation: int = 0, scale: pymunk.Vec2d = pymunk.Vec2d(1, 1)):
        Component.__init__(self)
        self.position = position
        self.rotation = rotation
        self.scale = scale

        self.first_update = True

    def update(self, dt):
        if self.first_update:
            self.first_update = False

            sprite = self.parent.get_component(SpriteRenderer)
            rigid = self.parent.get_component(RigidBody)

            if sprite is not None:
                sprite.sprite.position = self.position[0], self.position[1]
                sprite.sprite.rotation = math.degrees(-self.rotation)

                sprite.sprite.scale_x = self.scale[0]
                sprite.sprite.scale_y = self.scale[1]

            if rigid is not None:
                rigid.body.angle = math.radians(self.rotation)
                rigid.body.position = self.position

