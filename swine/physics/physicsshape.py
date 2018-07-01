#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from .physicsobject import PhysicsObject


class PhysicsShape(PhysicsObject):
    def __init__(self, scene, shape, x=0, y=0, mass=1, friction=0, angle=0, static=False, rotation=True, layer=0):
        points = [shape.points[i:i + 2] for i in range(0, len(shape.points), 2)]
        PhysicsObject.__init__(self, scene, x, y, mass, friction, angle, True, points, static, rotation, layer, False)
        self._shape = shape

    def physics_update(self, dt=None):
        points = []

        for v in self.shape.get_vertices():
            for i in v.rotated(self.shape.body.angle) + self.shape.body.position:
                points.append(i)

        self._shape.shape.vertices = points
