#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import enum


class Globals(object):
    FONT_FAMILY = "Courier"
    FONT_SIZE = 12

    FPS = 60
    FPS_LIMIT = 60

    WINDOW = None

    WIDGETS = 0


class Colour(enum.Enum):
    # Shades
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Primary
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Secondary
    PURPLE = (255, 0, 255)
    ORANGE = (255, 127, 0)
    GREEN = (0, 255, 0)


class Direction(enum.Enum):
    LEFT = -1
    RIGHT = 1
