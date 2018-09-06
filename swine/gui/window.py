#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kytten import Window as KWindow
from kytten.layout import ANCHOR_TOP_LEFT
from kytten.themes import felyne_dark


class Window(KWindow):
    def __init__(self, scene, title, content, x=0, y=0):
        KWindow.__init__(self, title, content,
                         window=scene.window, batch=scene.batch, offset=(x, y), theme=felyne_dark, anchor=ANCHOR_TOP_LEFT)

