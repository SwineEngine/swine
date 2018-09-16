#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple

from swine.component.physics.collider.base_collider import BaseCollider


class PolygonCollider(BaseCollider):
    def __init__(self: PolygonCollider, vertices: List[Tuple[float, float]] = None, trigger: bool = False, edge_radius: int = 0, friction: float = 0, elasticity: float = 0) -> None:
        self.vertices: List[Tuple[float, float]] = None

        self.width_verts = List[float] = None
        self.height_verts = List[float] = None
