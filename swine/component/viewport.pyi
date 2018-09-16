#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

from swine.object.component import Component


class Viewport(Component):
    def __init__(self: Viewport, size: pymunk.Vec2d = pymunk.Vec2d(640, 480), border=64) -> None:
        self.size: pymunk.Vec2d = None
        self.border: int = None

        self.x: int = None
        self.y: int = None
        self.angle: int = None

        self.first_update: bool = False
