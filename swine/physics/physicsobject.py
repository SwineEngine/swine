#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import pyglet
import pymunk

from swine import Globals
from swine.gameobject import GameObject


class PhysicsObject(GameObject):
    def __init__(self, scene, x=0, y=0, mass=1, friction=0, angle=0, vertices=[(-5, 5), (5, 5), (5, -5), (-5, -5)], static=False, rotation=True, layer=0):
        GameObject.__init__(self, scene, layer)
        x += scene.window.width / 2
        y += scene.window.height / 2
        self.mass = mass
        self.friction = friction
        self.obj_position = pymunk.Vec2d(x, y)
        self.angle = angle
        self.vertices = vertices
        self.static = static
        self.rotation = rotation

        self.momentum = pymunk.moment_for_poly(self.mass, self.vertices)

        self.body = pymunk.Body(self.mass, self.momentum if self.rotation else pymunk.inf)

        if self.static:
            self.body.body_type = pymunk.Body.STATIC

        self.shape = pymunk.Poly(body=self.body, vertices=self.vertices)
        self.shape.friction = self.friction
        self.shape.parent = self

        self.body.position = self.obj_position
        self.body.angle = self.angle

        self.scene.space.add(self.body, self.shape)

        self.scene.physics_list.append(self)

        self._interval = pyglet.clock.schedule_interval(self.physics_update, 1 / Globals.FPS)

    def physics_update(self, dt=None):
        pass

    def collision_enter(self, collider):
        pass

    def collision_stay(self, collider):
        pass

    def collision_exit(self, collider):
        pass
