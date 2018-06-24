#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from kytten.dialog import Dialog
from kytten.layout import GridLayout
from kytten.themes import felyne_dark

from swine import GameObject, Globals


class Widget(GameObject, Dialog):
    def __init__(self, scene, widget, x=0, y=0):
        GameObject.__init__(self, scene, -1)
        self.widget = widget
        self.widget.id = Globals.WIDGETS
        Globals.WIDGETS += 1

        Dialog.__init__(self, content=GridLayout(content=[
            [self.widget]
        ]),
            window=Globals.WINDOW, batch=scene.batch, group=scene.layers[-1], offset=(x, y), theme=felyne_dark)
