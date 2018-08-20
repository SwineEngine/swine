#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pyglet

from swine.input import Input
from swine.input.handler import MouseStateHandler


class InputManager(object):
    def __init__(self, window, joystick):
        self.window = window
        self.joystick = joystick

        self.inputs: List[Input] = []

        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.key_handler)

        self.mouse_handler = MouseStateHandler()
        self.window.push_handlers(self.mouse_handler)

    def get_key(self, key: int):
        return self.key_handler[key]

    def get_mouse_button(self, button: int):
        return self.mouse_handler.buttons.get(button)

    def get_mouse_position(self):
        pos = self.mouse_handler.position
        x = pos.get("x")
        y = pos.get("y")

        if x is not None:
            x -= self.window.width / 2

        if y is not None:
            y -= self.window.height / 2

        return x, y

    def get_joystick_button(self):
        print(self.joystick.buttons)
