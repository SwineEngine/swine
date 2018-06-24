#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from kytten import Menu as KMenu
from kytten import HALIGN_CENTER

from .widget import Widget


class Menu(Widget):
    def __init__(self, scene, options=[], command=None, align=HALIGN_CENTER, x=0, y=0):
        Widget.__init__(self, scene, KMenu(options, on_select=command), x, y)
