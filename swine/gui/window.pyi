#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from kytten import Window as KWindow, HorizontalLayout, VerticalLayout, GridLayout

from swine.gui import Canvas
from swine.object import GameObject, Component


class Window(KWindow, GameObject):
    def __init__(self: Window, canvas: Canvas, name: str, components: List[Component], title: str, content: HorizontalLayout or VerticalLayout or GridLayout, tags: List[str]=(), parent: GameObject=None) -> None:
        ...
