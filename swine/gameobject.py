#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import FPS, Scene


class GameObject(object):
    def __init__(self, scene, layer=0):
        # type: (Scene) -> None
        self._scene = scene
        self._layer = layer

        self.direction = 0

        self.window = self._scene._window
        self.keys = self.window._keys

        self.id = len(self._scene.object_list)
        self.tags = []

        pyglet.clock.schedule_interval(self.update, 1 / FPS)
        # pyglet.clock.schedule(self.update)

        self.start()

    def start(self):
        pass

    def update(self, dt=None):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_text(self, text):
        pass

    def on_text_motion(self, motion):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_mouse_enter(self, x, y):
        pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass
