#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Slider as KSlider

from swine.object import GameObject, Component
from .widget import Widget


class Slider(Widget, GameObject):
    def __init__(self, canvas, name, components: List[Component], tags: List[str]=(), parent=None, command=None, value=0, min_value=0, max_value=1, steps=None, width=100, disabled=False):
        Widget.__init__(self, canvas, KSlider(value=value, min_value=min_value, max_value=max_value, steps=steps, width=width, on_set=command, disabled=disabled), 0, 0)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
