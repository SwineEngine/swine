#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet


class Layer(object):
    def __init__(self, window, name, index=-1):
        self.window = window
        self.name = name

        if index == -1:
            self.index = len(self.window.layers)

        else:
            self.index = index

        self.window.layers.append(self)

        self.group = pyglet.graphics.OrderedGroup(self.index)
