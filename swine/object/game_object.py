#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from swine.object.component import Behaviour
from swine.window.scene import Scene


class GameObject(object):
    def __init__(self, scene: Scene, components: List[Behaviour]):
        self.scene = scene
        self.components = components

        self.scene.object_list.append(self)

        self.start()

    def start(self):
        for comp in self.components:
            comp.start()

    def update(self):
        for comp in self.components:
            comp.update()
