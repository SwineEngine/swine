#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import Scene


class GameObject(object):
    def __init__(self, scene):
        # type: (Scene) -> None
        self._scene = scene

        self.id = len(self._scene.draw_list)
        self.tags = []
