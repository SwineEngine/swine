#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Input as KInput

from swine.object import Component, GameObject
from .widget import Widget


class Input(Widget, GameObject):
    def __init__(self, canvas, name, components: List[Component], text, tags: List[str]=(), parent=None, command=None, length=10, limit=None, disabled=False):
        Widget.__init__(self, canvas, KInput(text, length=length, max_length=limit, on_input=command, disabled=disabled), 0, 0)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
