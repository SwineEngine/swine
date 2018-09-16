#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.graphics import OrderedGroup

from swine.window import Window


class Layer(object):
    def __init__(self: Layer, window: Window, name: str, index: int = -1) -> None:
        self.window: Window = None
        self.name: str = None

        self.index: int = None

        self.group: OrderedGroup = None
