#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from kytten import Input

from .widget import Widget


class Entry(Widget):
    def __init__(self, scene, text, length=10, limit=None, command=None, disabled=False, x=0, y=0):
        Widget.__init__(self, scene, Input(text, length=length, max_length=limit, on_input=command, disabled=disabled), x, y)
