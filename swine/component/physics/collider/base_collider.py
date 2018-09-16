#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.object import Component


class BaseCollider(Component):
    def __init__(self, trigger: bool = False, edge_radius: int = 0, friction: float = 0, elasticity: float = 0):
        Component.__init__(self)
        self.trigger = trigger
        self.edge_radius = edge_radius
        self.friction = friction
        self.elasticity = elasticity

        self.collider: pymunk.Shape = None
        self.width = 0
        self.height = 0

    def load(self):
        self.collider.friction = self.friction
        self.collider.elasticity = self.elasticity

        self.collider.parent = self

        self.parent.scene.space.add(self.collider)

    def unload(self):
        self.parent.scene.space.remove(self.collider)
