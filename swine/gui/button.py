#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from kytten.button import Button as KButton

from .widget import Widget


class Button(Widget):
    def __init__(self, scene, text, command=None, disabled=False, x=0, y=0):
        Widget.__init__(self, scene, KButton(text, on_click=command, disabled=disabled), x, y)
