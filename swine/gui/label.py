#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
from swine import Scene


class Label(pyglet.text.Label):
    def __init__(self, scene, text, x, y):
        # type: (Scene, str, int, int) -> None
        pyglet.text.Label.__init__(self, text=text, x=x, y=y)
        self._scene = scene
        self._text = text
        self._x = x
        self._y = y

        self._scene.draw_list.append(self)
