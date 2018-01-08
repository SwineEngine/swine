#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import Window


class Scene(object):
    def __init__(self, window):
        # type: (Window) -> None
        self.window = window

        self.index = 0
        self.draw_list = []

        self.window.scene_list.append(self)
