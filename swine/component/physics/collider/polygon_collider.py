#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple

import pymunk

from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.component.physics.collider import BaseCollider


class PolygonCollider(BaseCollider):
    def __init__(self, vertices: Tuple[Tuple[int]] = None, trigger: bool = False, edge_radius: int = 0, friction: float = 0, elasticity: float = 0):
        BaseCollider.__init__(self, trigger, edge_radius, friction, elasticity)
        self.vertices = vertices

    def start(self):
        rigid = self.parent.get_component(RigidBody)
        sprite = self.parent.get_component(SpriteRenderer)

        if sprite is not None and not self.vertices:
            width = sprite.sprite.width / 2
            height = sprite.sprite.height / 2

            self.vertices = [(-width, height),
                             (width, height),
                             (width, -height),
                             (-width, -height)]

        if rigid is not None:
            body = rigid.body

        else:
            body = None

        self.collider = pymunk.Poly(body, self.vertices, None, self.edge_radius)
        BaseCollider.start(self)
