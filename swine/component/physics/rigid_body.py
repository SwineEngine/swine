#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.object import Component


class RigidBody(Component):
    def __init__(self, mass=1, static=False, rotation=True):
        Component.__init__(self)

        self.mass = mass
        self.static = static
        self.rotation = rotation

        self.momentum = pymunk.moment_for_box(self.mass, (1, 1))
        self.body = None

    def load(self):
        self.body = pymunk.Body(self.mass, self.momentum if self.rotation else pymunk.inf)

        if self.static:
            self.body.body_type = pymunk.Body.STATIC

        self.parent.scene.space.add(self.body)

    def unload(self):
        self.parent.scene.space.remove(self.body)

    def add_force(self, x, y):
        self.body.force = pymunk.Vec2d(x, y)
