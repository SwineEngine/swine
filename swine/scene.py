#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import Window


class Scene(object):
    def __init__(self, window, layer_count=25):
        # type: (Window) -> None
        self.window = window
        self.layer_count = layer_count

        self.id = len(self.window.scene_list)
        self.batch = pyglet.graphics.Batch()
        self.batch_list = [self.batch]
        self.object_list = []

        self.layers = []
        for number in range(self.layer_count):
            self.layers.append(pyglet.graphics.OrderedGroup(number))

        self.window.scene_list.append(self)


