#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pymunk

from swine.component.physics.rigid_body import RigidBody
from swine.component.sprite_renderer import SpriteRenderer
from swine.object.component import Component


class Transform(Component):
    def __init__(self: Transform, position: pymunk.Vec2d = pymunk.Vec2d(0, 0), rotation: int = 0, scale: pymunk.Vec2d = pymunk.Vec2d(1, 1)):
        self.position: pymunk.Vec2d = None
        self.rotation: int = None
        self.scale: pymunk.Vec2d = None

        self.first_update: bool = None
        self.move_to_rigid: bool = None

        self.sprites: List[SpriteRenderer] = None
        self.rigid: RigidBody = None

    def move_rigid_to_parent(self: Transform) -> None:
        ...
