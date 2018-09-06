#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kytten.dialog import Dialog
from kytten.layout import GridLayout
from kytten.themes import felyne_dark


class Widget(Dialog):
    def __init__(self, scene, widget, x=0, y=0):
        self.widget = widget

        Dialog.__init__(self, content=GridLayout(content=[
            [self.widget]
        ]),
            window=scene.window, batch=scene.batch, offset=(x, y), theme=felyne_dark)

    def on_text(self, text):
        pass
