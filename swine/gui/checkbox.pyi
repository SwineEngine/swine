#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import List

from swine.gui import Canvas
from swine.object import Component, GameObject
from .widget import Widget


class Checkbox(Widget, GameObject):
    def __init__(self: Checkbox, canvas: Canvas, name: str, components: List[Component], text: str, tags: List[str]=(), parent: GameObject=None, command: FunctionType=None, is_checked: bool=False, disabled: bool=False) -> None:
        ...
