#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kytten import Slider as KSlider

from .widget import Widget


class Slider(Widget):
    def __init__(self, scene, command=None, value=0, min_value=0, max_value=1, steps=None, width=100, disabled=False, x=0, y=0):
        Widget.__init__(self, scene, KSlider(value=value, min_value=min_value, max_value=max_value, steps=steps, width=width, on_set=command, disabled=disabled), x, y)
