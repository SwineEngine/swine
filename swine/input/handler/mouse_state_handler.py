#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MouseStateHandler(object):
    def __init__(self):
        self.buttons = {}
        self.position = {}

    def on_mouse_press(self, x, y, symbol, modifiers):
        self.buttons[symbol] = True

    def on_mouse_release(self, x, y, symbol, modifiers):
        self.buttons[symbol] = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.position["x"] = x
        self.position["y"] = y
