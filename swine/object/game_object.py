#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Optional, Type

import pyglet

from swine.object.component import Component
from swine.window.scene import Scene


class GameObject(object):
    def __init__(self, scene: Scene, components: List[Component]):
        self.scene = scene
        self.components = components

        self.id: int = 0

        self.tags: List[str] = []

        self.scene.object_list.append(self)

        self.start()
        self._interval = pyglet.clock.schedule(self.update)
        self._interval = pyglet.clock.schedule(self.physics_update)

    def start(self):
        for comp in self.components:
            comp.parent = self
            comp.start()

    def update(self, dt=None):
        for comp in self.components:
            comp.update(dt)

    def physics_update(self, dt=None):
        for comp in self.components:
            comp.physics_update(dt)

    def get_component(self, type_: Component) -> Optional[Type[Component]]:
        for comp in self.components:
            if type(comp) == type_:
                return comp

        return None
