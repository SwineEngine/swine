#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import Window
from swine import FPS


class Scene(object):
    def __init__(self, window):
        # type: (Window) -> None
        self._window = window

        self.id = len(self._window.scene_list)
        self.batch = pyglet.graphics.Batch()
        self.object_list = []

        self._window.scene_list.append(self)


