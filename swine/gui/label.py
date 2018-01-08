#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
from swine import Scene


class Label(pyglet.text.Label):
    def __init__(self, scene, text, x, y):
        # type: (Scene, str, int, int) -> None
        pyglet.text.Label.__init__(self, text=text, x=x, y=y)
        self.scene = scene
        self.text = text
        self.x = x
        self.y = y

        self.scene.draw_list.append(self)
