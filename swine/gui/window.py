#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from kytten import Window as KWindow
from kytten.layout import ANCHOR_TOP_LEFT
from kytten.themes import felyne_dark

from swine import GameObject, Globals


class Window(GameObject, KWindow):
    def __init__(self, scene, title, content, x=0, y=0):
        GameObject.__init__(self, scene, -1)
        KWindow.__init__(self, title, content,
                         window=Globals.WINDOW, batch=scene.batch, group=scene.layers[-1], offset=(x, y), theme=felyne_dark, anchor=ANCHOR_TOP_LEFT)

