#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.input import EmptyController


class XBoxController(EmptyController):
    LEFT_TRIGGER = "z"
    RIGHT_TRIGGER = "z"

    LEFT_BUMPER = 4
    RIGHT_BUMPER = 5

    BACK = 6
    MENU = 7

    X = 3
    Y = 2
    B = 1
    A = 0

    DIRECTIONAL_PAD_LEFT = (-1, 0)
    DIRECTIONAL_PAD_RIGHT = (1, 0)
    DIRECTIONAL_PAD_UP = (0, 1)
    DIRECTIONAL_PAD_DOWN = (0, -1)

    LEFT_THUMBSTICK = 8
    LEFT_THUMBSTICK_X = "x"
    LEFT_THUMBSTICK_Y = "y"

    RIGHT_THUMBSTICK = 9
    RIGHT_THUMBSTICK_X = "rx"
    RIGHT_THUMBSTICK_Y = "ry"
