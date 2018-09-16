#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Window as KWindow
from kytten.layout import ANCHOR_TOP_LEFT
from kytten.themes import felyne_dark

from swine.object import GameObject, Component


class Window(KWindow, GameObject):
    def __init__(self, canvas, name, components, title, content, tags=(), parent=None):
        KWindow.__init__(self, title, content,
                         window=canvas.scene.window, batch=canvas.batch, offset=(0, 0), theme=felyne_dark, anchor=ANCHOR_TOP_LEFT)
        GameObject.__init__(self, canvas.scene, name, components, tags, parent)

