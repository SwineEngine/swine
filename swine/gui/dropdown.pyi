#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import List

from swine.gui import Canvas
from swine.object import GameObject, Component
from .widget import Widget


class Dropdown(Widget, GameObject):
    def __init__(self: Dropdown, canvas: Canvas, name: str, components: List[Component], options: List[str], tags: List[str]=(), parent: GameObject=None, command: FunctionType=None, selected: str=None, max_height: int=400, disabled: bool=False) -> None:
        ...
