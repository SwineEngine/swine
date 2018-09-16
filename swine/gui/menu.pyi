#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import List

from kytten import HALIGN_CENTER

from swine.gui import Canvas
from swine.object import GameObject, Component
from .widget import Widget


class Menu(Widget, GameObject):
    def __init__(self: Menu, canvas: Canvas, name: str, components: List[Component], options: List[str], tags: List[str]=(), parent: GameObject=None, command: FunctionType=None, align: int=HALIGN_CENTER) -> None:
        ...
