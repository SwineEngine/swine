#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten.checkbox import Checkbox as KCheckbox

from swine.object import Component, GameObject
from .widget import Widget


class Checkbox(Widget, GameObject):
    def __init__(self, canvas, name, components, text, tags=(), parent=None, command=None, is_checked=False, disabled=False):
        Widget.__init__(self, canvas, KCheckbox(text, on_click=command, is_checked=is_checked, disabled=disabled), 0, 0)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
