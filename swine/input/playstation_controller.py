#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum

from swine.input import EmptyController


class PlayStationController(EmptyController):
    LEFT_TRIGGER_PRESS = 6
    LEFT_TRIGGER = "rz"
    RIGHT_TRIGGER_PRESS = 7
    RIGHT_TRIGGER = "rz"

    LEFT_BUMPER = 4
    RIGHT_BUMPER = 5

    SHARE = 8
    OPTIONS = 9

    SQUARE = 0
    TRIANGLE = 3
    CROSS = 1
    CIRCLE = 2

    DIRECTIONAL_PAD_LEFT = (-1, 0)
    DIRECTIONAL_PAD_RIGHT = (1, 0)
    DIRECTIONAL_PAD_UP = (0, 1)
    DIRECTIONAL_PAD_DOWN = (0, -1)

    LEFT_THUMBSTICK = 10
    LEFT_THUMBSTICK_X = "x"
    LEFT_THUMBSTICK_Y = "y"

    RIGHT_THUMBSTICK = 11
    RIGHT_THUMBSTICK_X = "rx"
    RIGHT_THUMBSTICK_Y = "ry"

    HOME = 12

    TOUCH_PAD_PRESS = 13
