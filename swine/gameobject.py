#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import FPS, Scene, Direction


class GameObject(object):
    def __init__(self, scene, layer=0):
        # type: (Scene) -> None
        self.scene = scene
        self.layer = layer

        self.direction = Direction.RIGHT

        self.window = self.scene.window
        self.keys = self.window.keys

        self.id = len(self.scene.object_list)
        self.tags = []

        self._interval = pyglet.clock.schedule_interval(self.update, 1 / FPS)
        # pyglet.clock.schedule(self.update)

        self.scene.object_list.append(self)

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

    #####

    def destroy(self):
        pyglet.clock.unschedule(self._interval)
        self.scene.object_list.remove(self)
