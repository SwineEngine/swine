#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import FPS, Scene


class GameObject(object):
    def __init__(self, scene, layer=0):
        # type: (Scene) -> None
        self._scene = scene
        self._layer = layer

        self.window = self._scene._window
        self.keys = self.window._keys

        self.id = len(self._scene.object_list)
        self.tags = []

        pyglet.clock.schedule_interval(self.update, 1 / FPS)

        self.start()

    def start(self, event=None):
        pass

    def update(self, event=None):
        pass
