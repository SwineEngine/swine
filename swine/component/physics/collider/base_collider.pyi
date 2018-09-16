#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymunk import Shape

from swine.object.component import Component


class BaseCollider(Component):
    def __init__(self: BaseCollider, trigger: bool = False, edge_radius: int = 0, friction: float = 0, elasticity: float = 0) -> None:
        self.trigger: bool = None
        self.edge_radius: int = None
        self.friction: float = None
        self.elasticity: float = None

        self.collider: Shape = None
        self.width: float = None
        self.height: float = None
