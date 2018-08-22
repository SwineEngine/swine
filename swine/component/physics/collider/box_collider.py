#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.component.physics.collider import BaseCollider


class BoxCollider(BaseCollider):
    def __init__(self, left: pymunk.Vec2d = None, right: pymunk.Vec2d = None, trigger: bool = False, edge_radius: int = None, friction: float = 0, elasticity: float = 0):
        BaseCollider.__init__(self, trigger, edge_radius, friction, elasticity)
        self.left = left
        self.right = right

    def start(self):
        rigid = self.parent.get_component(RigidBody)
        sprite = self.parent.get_component(SpriteRenderer)

        if sprite is not None and self.left is None and self.right is None and self.edge_radius is None:
            self.left = pymunk.Vec2d(0, sprite.sprite.height / 2)
            self.right = pymunk.Vec2d(0, -sprite.sprite.height / 2)
            self.edge_radius = sprite.sprite.width / 2

        if rigid is not None:
            body = rigid.body

        else:
            body = None

        self.collider = pymunk.Segment(body, self.left, self.right, self.edge_radius)
        BaseCollider.start(self)
