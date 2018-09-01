#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum

from swine.input import EmptyController


class GameCubeController(EmptyController):
    LEFT_TRIGGER = 4
    RIGHT_TRIGGER = 5

    START = 9

    X = 1
    Y = 0
    A = 2
    B = 3

    Z = 6

    DIRECTIONAL_PAD_LEFT = (-1, 0)
    DIRECTIONAL_PAD_RIGHT = (1, 0)
    DIRECTIONAL_PAD_UP = (0, 1)
    DIRECTIONAL_PAD_DOWN = (0, -1)

    THUMBSTICK_X = "x"
    THUMBSTICK_Y = "y"

    CTHUMBSTICK_X = "z"
    CTHUMBSTICK_Y = "rz"
