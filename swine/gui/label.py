#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
from swine import GameObject, Scene


class Label(GameObject, pyglet.text.Label):
    def __init__(self, scene, text, x, y):
        # type: (Scene, str, int, int) -> None
        pyglet.text.Label.__init__(self, text=text, x=x, y=y, batch=scene.batch)
        self._scene = scene
        self._text = text
        self._x = x
        self._y = y

        self._scene.object_list.append(self)

    def update(self, event=None):
        self.x += 1
