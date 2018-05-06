#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import Window


class Scene(object):
    def __init__(self, window, layers=25):
        # type: (Window) -> None
        self._window = window
        self._layers = layers

        self.id = len(self._window.scene_list)
        self.batch = pyglet.graphics.Batch()
        self.batch_list = [self.batch]
        self.object_list = []

        self.layers = []
        for number in range(self._layers):
            self.layers.append(pyglet.graphics.OrderedGroup(number))

        self._window.scene_list.append(self)


