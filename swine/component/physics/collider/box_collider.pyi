#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.component.physics.collider.base_collider import BaseCollider


class BoxCollider(BaseCollider):
    def __init__(self: BoxCollider, left: pymunk.Vec2d = None, right: pymunk.Vec2d = None, trigger: bool = False, edge_radius: int = None, friction: float = 0, elasticity: float = 0) -> None:
        self.left: float = None
        self.right: float = None
