#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple

from swine.gui import Widget, Canvas
from swine.object import GameObject, Component


class Label(Widget, GameObject):
    def __init__(self: Label, canvas: Canvas, name: str, components: List[Component], text: str, bold: bool=False, italic: bool=False, colour: Tuple[int, int, int, int]=(255, 255, 255, 255), tags: List[str]=(), parent: GameObject=None):
        ...
