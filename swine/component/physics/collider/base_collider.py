#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple

import pymunk

from swine.object import Component


class BaseCollider(Component):
    def __init__(self, vertices: Tuple[Tuple[int]] = None, trigger: bool = False, edge_radius: int = 0, friction: float = 0, elasticity: float = 0):
        Component.__init__(self)
        self.vertices = vertices
        self.trigger = trigger
        self.edge_radius = edge_radius
        self.friction = friction
        self.elasticity = elasticity

        self.collider: pymunk.Shape = None

    def start(self):
        self.collider.friction = self.friction
        self.collider.elasticity = self.elasticity

        self.collider.parent = self

        self.parent.scene.space.add(self.collider)
