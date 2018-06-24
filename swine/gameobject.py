#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import Globals, Scene, RIGHT


class GameObject(object):
    def __init__(self, scene, layer=0):
        # type: (Scene) -> None
        self.scene = scene
        self.layer = layer

        self.direction = RIGHT

        self.window = self.scene.window
        self.keys = self.window.keys

        self.id = len(self.scene.object_list)
        self.tags = []

        if Globals.OBJECT_FPS != -1:
            self._interval = pyglet.clock.schedule_interval(self.update, 1 / Globals.OBJECT_FPS)

        else:
            self._interval = pyglet.clock.schedule(self.update)

        # pyglet.clock.schedule(self.update)

        self.scene.object_list.append(self)

        self.start()

    def start(self):
        pass

    def update(self, dt=None):
        pass

    def key_press(self, symbol, modifiers):
        pass

    def key_release(self, symbol, modifiers):
        pass

    def text(self, text):
        pass

    def text_motion(self, motion):
        pass

    def mouse_motion(self, x, y, dx, dy):
        pass

    def mouse_press(self, x, y, button, modifiers):
        pass

    def mouse_release(self, x, y, button, modifiers):
        pass

    def mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def mouse_enter(self, x, y):
        pass

    def mouse_leave(self, x, y):
        pass

    def mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    #####

    def destroy(self):
        pyglet.clock.unschedule(self._interval)
        self.scene.object_list.remove(self)
