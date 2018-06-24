#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from kytten.checkbox import Checkbox as KCheckbox

from .widget import Widget


class Checkbox(Widget):
    def __init__(self, scene, text, command=None, is_checked=False, disabled=False, x=0, y=0):
        Widget.__init__(self, scene, KCheckbox(text, on_click=command, is_checked=is_checked, disabled=disabled), x, y)
