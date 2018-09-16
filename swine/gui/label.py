#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from kytten.widgets import Label as KLabel

from swine.gui import Widget
from swine.object import GameObject, Component


class Label(Widget, GameObject):
    def __init__(self, canvas, name, components, text, bold=False, italic=False, colour=(255, 255, 255, 255), tags=(), parent=None):
        Widget.__init__(self, canvas, KLabel(text, font_name=None, font_size=None, bold=bold, italic=italic, color=colour))
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)
