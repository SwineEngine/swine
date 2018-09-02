#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple

import pyglet

from swine.input import EmptyController
from swine.input.handler import MouseStateHandler, JoyStickStateHandler


class InputManager(object):
    def __init__(self, window, joystick):
        self.window = window
        self.joystick = joystick

        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.key_handler)

        self.mouse_handler = MouseStateHandler()
        self.window.push_handlers(self.mouse_handler)

        if self.joystick is not None:
            self.joystick_handler = JoyStickStateHandler()
            self.joystick.push_handlers(self.joystick_handler)

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

    def get_joystick_button(self, button: int):
        if isinstance(button, EmptyController):
            button = button.value

        return self.joystick_handler.button.get(button)

    def get_joystick_hat(self, vector: Tuple[int]):
        if self.joystick is not None:
            if isinstance(vector, EmptyController):
                vector = vector.value

            if self.joystick_handler.hat == vector:
                return True

            else:
                return False

        else:
            return False

    def get_joystick_axis(self, axis: str):
        if self.joystick is not None:
            if isinstance(axis, EmptyController):
                axis = axis.value

            return self.joystick_handler.axis.get(axis)

        else:
            return 0
