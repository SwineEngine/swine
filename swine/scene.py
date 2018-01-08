#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import Window


class Scene(object):
    def __init__(self, window):
        # type: (Window) -> None
        self._window = window

        self.id = len(self._window.scene_list)
        self.draw_list = []

        self._window.scene_list.append(self)
