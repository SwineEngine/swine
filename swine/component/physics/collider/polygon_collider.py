#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.component import SpriteRenderer
from swine.component.physics.collider import BaseCollider


class PolygonCollider(BaseCollider):
    def __init__(self, vertices=(), trigger=False, edge_radius=0, friction=0, elasticity=0):
        BaseCollider.__init__(self, trigger, edge_radius, friction, elasticity)
        self.vertices = vertices

        self.width_verts = None
        self.height_verts = None

    def start(self):
        from swine.component.physics import RigidBody

        rigid = self.parent.get_component(RigidBody)
        sprite = self.parent.get_component(SpriteRenderer)

        if sprite is not None and not self.vertices:
            width = sprite.sprite.width / 2
            height = sprite.sprite.height / 2

            self.vertices = [(-width, height),
                             (width, height),
                             (width, -height),
                             (-width, -height)]

        self.width_verts = [i[0] for i in self.vertices]
        self.height_verts = [i[1] for i in self.vertices]

        if rigid is not None:
            body = rigid.body

        else:
            body = None

        positive_width = [abs(n) for n in self.width_verts]
        positive_height = [abs(n) for n in self.height_verts]

        self.width = min(positive_width) + max(positive_width)
        self.height = min(positive_height) + max(positive_height)

        self.collider = pymunk.Poly(body, self.vertices, None, self.edge_radius)
