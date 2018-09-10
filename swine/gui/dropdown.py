#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Dropdown as KDropdown

from swine.object import GameObject, Component
from .widget import Widget


class Dropdown(Widget, GameObject):
    def __init__(self, canvas, name, components: List[Component], options, tags: List[str]=(), parent=None, command=None, selected=None, max_height=400, disabled=False):
        Widget.__init__(self, canvas, KDropdown(options, selected=selected, max_height=max_height, on_select=command, disabled=disabled), 0, 0)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
