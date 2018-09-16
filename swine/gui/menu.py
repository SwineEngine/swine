#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Menu as KMenu
from kytten import HALIGN_CENTER

from swine.object import GameObject, Component
from .widget import Widget


class Menu(Widget, GameObject):
    def __init__(self, canvas, name, components, options, tags=(), parent=None, command=None, align=HALIGN_CENTER):
        Widget.__init__(self, canvas, KMenu(options, align, on_select=command), 0, 0)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
