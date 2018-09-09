#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Optional, Type

import pyglet
import pymunk

from swine.object.component import Component
from swine.window.scene import Scene
from swine.component import Transform


class GameObject(object):
    def __init__(self, scene: Scene, name: str, components: List[Component], tags: List[str] = (), parent=None):
        self.scene = scene
        self.name = name
        self.components = components

        self.parent = parent
        self.children = []

        self.id: int = 0

        self.tags: List[str] = tags

        self.scene.object_list.append(self)

        self.start()
        self._interval = pyglet.clock.schedule(self.update)
        self._interval = pyglet.clock.schedule(self.physics_update)

    # Listeners

    def start(self):
        for comp in self.components:
            comp.parent = self
            comp.start()

        if self.parent is not None:
            self.set_parent(self.parent)

    def update(self, dt=None):
        for comp in self.components:
            comp.update(dt)

    def physics_update(self, dt=None):
        for comp in self.components:
            comp.physics_update(dt)

    def collision_enter(self, collider):
        for comp in self.components:
            comp.collision_enter(collider)

    def collision_stay(self, collider):
        for comp in self.components:
            comp.collision_stay(collider)

    def collision_exit(self, collider):
        for comp in self.components:
            comp.collision_exit(collider)

    # Methods

    def set_parent(self, parent):
        self.parent = parent
        if self.parent is not None:
            self.scene.object_list[self.scene.object_list.index(self.parent)].children.append(self)

    def get_component(self, type_: Type[Component]) -> Optional[Component]:
        for comp in self.components:
            if type(comp) == type_:
                return comp

        return None
