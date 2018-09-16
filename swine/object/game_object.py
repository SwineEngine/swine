#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Optional, Type

import pyglet
import pymunk

from swine.object.component import Component


class GameObject(object):
    def __init__(self, scene, name: str, components: List[Component], tags: List[str] = (), parent=None, never_reload=False):
        self.scene = scene
        self.name = name
        self.components = components
        self.never_reload = never_reload

        self.pre_load = True
        self.is_loaded = True

        self.parent = parent
        self.children = []

        self.id: int = 0

        self.tags: List[str] = tags

        self.scene.object_list.append(self)

        self.start()

        pyglet.clock.schedule(self.update)
        pyglet.clock.schedule(self.physics_update)

    # Listeners

    def start(self):
        for comp in self.components:
            comp.parent = self

        if self.parent is not None:
            self.set_parent(self.parent)

        self.load()

    def update(self, dt=None):
        if self.pre_load:
            self.pre_load = False

            for comp in self.components:
                comp.update(dt)

            return

        from swine.component import Transform
        from swine.component import Viewport

        transform = self.get_component(Transform)
        camera = self.scene.get_object_with_component(Viewport)

        if camera is not None:
            camera_viewport = camera.get_component(Viewport)
            camera_transform = camera.get_component(Transform)

            if transform is not None:
                if camera_transform is not None:
                    # TODO: Take the transforms size into account
                    if transform.position.x < camera_transform.position.x - camera_viewport.size.x / 2 - camera_viewport.border or transform.position.x > camera_transform.position.x + camera_viewport.size.x / 2 + camera_viewport.border \
                            or transform.position.y < camera_transform.position.y - camera_viewport.size.y / 2 - camera_viewport.border or transform.position.y > camera_transform.position.y + camera_viewport.size.y / 2 + camera_viewport.border:
                        if self.is_loaded:
                            self.unload()

                    else:
                        if not self.is_loaded:
                            self.load()

        if self.is_loaded:
            for comp in self.components:
                if comp.is_loaded or type(comp):
                    comp.update(dt)

    def physics_update(self, dt=None):
        if self.is_loaded:
            for comp in self.components:
                if comp.is_loaded:
                    comp.physics_update(dt)

    def collision_enter(self, collider):
        if self.is_loaded:
            for comp in self.components:
                if comp.is_loaded:
                    comp.collision_enter(collider)

    def collision_stay(self, collider):
        if self.is_loaded:
            for comp in self.components:
                if comp.is_loaded:
                    comp.collision_stay(collider)

    def collision_exit(self, collider):
        if self.is_loaded:
            for comp in self.components:
                if comp.is_loaded:
                    comp.collision_exit(collider)

    # Methods

    def load(self):
        self.is_loaded = True

        for comp in self.components:
            comp.start()
            comp.is_loaded = True
            comp.load()

    def unload(self):
        self.is_loaded = False

        if self.never_reload:
            pyglet.clock.unschedule(self.update)
            pyglet.clock.unschedule(self.physics_update)

        for comp in self.components:
            comp.finish()
            comp.is_loaded = False
            comp.unload()

    def flip_load(self):
        self.is_loaded = not self.is_loaded

        if self.is_loaded:
            self.load()

        else:
            self.unload()

    def set_parent(self, parent):
        self.parent = parent
        if self.parent is not None:
            self.scene.object_list[self.scene.object_list.index(self.parent)].children.append(self)

    def get_component(self, type_: Type[Component]) -> Optional[Component]:
        for comp in self.components:
            if type(comp) == type_:
                return comp

        return None
