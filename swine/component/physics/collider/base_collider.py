#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.object import Component


class BaseCollider(Component):
    def __init__(self, trigger=False, edge_radius=0, friction=0, elasticity=0):
        Component.__init__(self)
        self.trigger = trigger
        self.edge_radius = edge_radius
        self.friction = friction
        self.elasticity = elasticity

        self.collider = None
        self.width = 0
        self.height = 0

    def load(self):
        self.collider.friction = self.friction
        self.collider.elasticity = self.elasticity

        self.collider.parent = self

        self.parent.scene.space.add(self.collider)

    def unload(self):
        self.parent.scene.space.remove(self.collider)
