#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


class GameObject(object):
    def __init__(self, scene):
        self.scene = scene

        self.id = len(self.scene.draw_list)
        self.tags = []
