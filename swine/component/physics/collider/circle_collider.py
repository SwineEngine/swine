#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.component.physics.collider import BaseCollider


class CircleCollider(BaseCollider):
    def __init__(self, radius: int = 1, trigger: bool = False, friction: float = 0, elasticity: float = 0):
        BaseCollider.__init__(self, trigger, 0, friction, elasticity)
        self.radius = radius

    def start(self):
        from swine.component.physics import RigidBody

        rigid = self.parent.get_component(RigidBody)

        if rigid is not None:
            body = rigid.body

        else:
            body = None

        self.width = self.radius
        self.height = self.radius

        self.collider = pymunk.Circle(body, self.radius)
