#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from swine import Scene


class GameObject(object):
    def __init__(self, scene):
        # type: (Scene) -> None
        self._scene = scene

        self.id = len(self._scene.object_list)
        self.tags = []

        self.start()

    def start(self, event=None):
        pass

    def update(self, event=None):
        pass
