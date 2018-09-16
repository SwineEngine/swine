#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import List

from swine.gui import Canvas
from swine.object import GameObject, Component
from .widget import Widget


class Slider(Widget, GameObject):
    def __init__(self: Slider, canvas: Canvas, name: str, components: List[Component], tags: List[str]=(), parent: GameObject=None, command: FunctionType=None, value: int=0, min_value: float=0, max_value: float=1, steps: float=None, width: float=100, disabled: bool=False) -> None:
        ...
