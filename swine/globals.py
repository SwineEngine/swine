#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import enum

FONT_FAMILY = "Courier"
FONT_SIZE = 12

FPS = 60
FPS_LIMIT = 60


class Direction(enum.Enum):
    LEFT = -1
    RIGHT = 1
