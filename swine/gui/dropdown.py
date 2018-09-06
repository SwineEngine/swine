#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kytten import Dropdown as KDropdown

from .widget import Widget


class Dropdown(Widget):
    def __init__(self, scene, options=[], command=None, selected=None, max_height=400, disabled=False, x=0, y=0):
        Widget.__init__(self, scene, KDropdown(options, selected=selected, max_height=max_height, on_select=command, disabled=disabled), x, y)
