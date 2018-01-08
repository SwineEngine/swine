#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
from swine import Window


class Label(pyglet.text.Label):
    def __init__(self, window, text, x, y):
        # type: (Window, str, int, int) -> None
        super().__init__(text=text, x=x, y=y)
