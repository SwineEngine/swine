#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
from swine import GameObject, Scene


class Label(GameObject, pyglet.text.Label):
    def __init__(self, scene, text="", x=0, y=0):
        # type: (Scene, str, int, int) -> None
        GameObject.__init__(self, scene=scene)
        pyglet.text.Label.__init__(self, text=text, x=x, y=y, batch=scene.batch)
        self._scene = scene
        self._text = text
        self._x = x
        self._y = y

        self._scene.object_list.append(self)
