#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple

from pyglet.input import Joystick
from pyglet.window.key import KeyStateHandler

from swine.input.handler import MouseStateHandler, JoyStickStateHandler
from swine.window.window import Window


class InputManager(object):
    def __init__(self: InputManager, window: Window, joystick: Joystick):
        self.window: Window = None
        self.joystick: Joystick = None

        self.key_handler: KeyStateHandler = None

        self.mouse_handler: MouseStateHandler = None

        self.joystick_handler: JoyStickStateHandler = None

    def get_key(self: InputManager, key: int) -> bool:
        ...

    def get_mouse_button(self: InputManager, button: int) -> bool:
        ...

    def get_mouse_position(self: InputManager) -> Tuple[float, float]:
        ...

    def get_joystick_button(self: InputManager, button: int) -> bool:
        ...

    def get_joystick_hat(self: InputManager, vector: Tuple[int]) -> Tuple[bool, bool]:
        ...

    def get_joystick_axis(self: InputManager, axis: str) -> float:
        ...
