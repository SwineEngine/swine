#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pyglet.graphics import Batch

from swine.object import GameObject
from swine.object.component import Component
from swine.window.scene import Scene


class Canvas(GameObject):
    def __init__(self: Canvas, scene: Scene, name: str, components: List[Component], tags: List[str]=()) -> None:
        self.batch: Batch = None
