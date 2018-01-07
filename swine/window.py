#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

class Window(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self)

        self._fullscreen = False
        self._min_size = (0, 0)
        self._max_size = (0, 0)

    def title(self, title):
        # type: (str) -> str
        self.set_caption(title)

        return self.get_caption()

    def fullscreen(self, fullscreen):
        # type: (bool) -> bool
        self._fullscreen = fullscreen
        self.set_fullscreen(fullscreen)

        return self._fullscreen

    def min_size(self, width, height):
        # type: (int, int) -> tuple[int, int]
        self._min_size = (width, height)
        self.set_minimum_size(width, height)

        return self._min_size

    def max_size(self, width, height):
        # type: (int, int) -> tuple[int, int]
        self._max_size = (width, height)
        self.set_maximum_size(width, height)

        return self._max_size

    def size(self, width, height):
        # type: (int, int) -> tuple[int, int]
        self.set_size(width, height)

        return self.get_size()

    def location(self, x, y):
        # type: (int, int) -> tuple[int, int]
        self.set_location(x, y)

        return self.get_location()

    def geometry(self):
        pass

    def on_draw(self):
        self.clear()
