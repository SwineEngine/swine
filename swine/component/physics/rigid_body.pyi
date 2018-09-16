#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymunk import Body

from swine.object.component import Component


class RigidBody(Component):
    def __init__(self: RigidBody, mass: int = 1, static: bool = False, rotation: bool = True) -> None:
        self.mass: int = None
        self.static: bool = None
        self.rotation: bool = None

        self.momentum: float = None
        self.body: Body = None

    def add_force(self: RigidBody, x: float, y: float):
        ...