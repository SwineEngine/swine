#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.component.physics.collider import BoxCollider, PolygonCollider, CircleCollider
from swine.object import Component


class RigidBody(Component):
    def __init__(self, mass=1, static=False, rotation=True):
        Component.__init__(self)
        self.mass = mass
        self.static = static
        self.rotation = rotation

        self.collider = None

        self.momentum = None
        self.body = None

    def start(self):
        box = self.parent.get_component(BoxCollider)
        poly = self.parent.get_component(PolygonCollider)
        circle = self.parent.get_component(CircleCollider)

        if box:
            self.collider = box

        elif poly:
            self.collider = poly

        elif circle:
            self.collider = circle

    def load(self):
        # self.momentum = pymunk.moment_for_box(self.mass, (1, 1))
        if type(self.collider) == BoxCollider:
            self.momentum = pymunk.moment_for_box(self.mass, (self.collider.width, self.collider.height))

        elif type(self.collider) == PolygonCollider:
            self.momentum = pymunk.moment_for_poly(self.mass, self.collider.vertices)

        elif type(self.collider) == CircleCollider:
            self.momentum = pymunk.moment_for_circle(self.mass, self.collider.radius, self.collider.radius)

        self.body = pymunk.Body(self.mass, self.momentum if self.rotation else pymunk.inf)

        if self.static:
            self.body.body_type = pymunk.Body.STATIC

        self.parent.scene.space.add(self.body)

    def unload(self):
        self.parent.scene.space.remove(self.body)

    def add_force(self, x, y):
        self.body.force = pymunk.Vec2d(x, y)
