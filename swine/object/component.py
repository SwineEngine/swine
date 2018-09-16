#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Component(object):
    def __init__(self):
        self.parent = None

        self.is_loaded = None

    def start(self):
        pass

    def update(self, dt):
        pass

    def finish(self):
        pass

    def physics_update(self, dt):
        pass

    def collision_enter(self, collider):
        pass

    def collision_stay(self, collider):
        pass

    def collision_exit(self, collider):
        pass

    def draw(self):
        pass

    def load(self):
        pass

    def unload(self):
        pass
