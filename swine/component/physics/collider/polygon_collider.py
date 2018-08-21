#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.component.physics.collider import BaseCollider


class PolygonCollider(BaseCollider):
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
