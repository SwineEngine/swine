#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Button as KButton

from swine.object import GameObject, Component
from .widget import Widget


class Button(Widget, GameObject):
    def __init__(self, canvas, name, components: List[Component], text, tags: List[str]=(), parent=None, command=None, disabled=False):
        Widget.__init__(self, canvas, KButton(text, on_click=command, disabled=disabled), 0, 0)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
