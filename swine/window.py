#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

class Window(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self)

    def title(self, title):
        self.set_caption(title)

    def on_draw(self):
        self.clear()
