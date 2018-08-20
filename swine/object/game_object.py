#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from swine.object.component import Component
from swine.window.layers import Layers
from swine.window.scene import Scene


class GameObject(object):
    def __init__(self, scene: Scene, components: List[Component]):
        self.scene = scene
        self.components = components

        self.scene.object_list.append(self)

        self.start()

    def start(self):
        for comp in self.components:
            comp.parent = self
            comp.start()

    def update(self):
        for comp in self.components:
            comp.update()
