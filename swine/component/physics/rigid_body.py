#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.object import Component


class RigidBody(Component):
    def __init__(self, mass: int = 1, static: bool = False, rotation: bool = True):
        Component.__init__(self)

        self.mass = mass
        self.static = static
        self.rotation = rotation

        self.momentum = pymunk.moment_for_box(self.mass, (1, 1))
        self.body: pymunk.Body = None

    def load(self):
        self.body = pymunk.Body(self.mass, self.momentum if self.rotation else pymunk.inf)

        if self.static:
            self.body.body_type = pymunk.Body.STATIC

        self.parent.scene.space.add(self.body)

    def unload(self):
        self.parent.scene.space.remove(self.body)

    def add_force(self, x: float, y: float):
        self.body.force = pymunk.Vec2d(x, y)
