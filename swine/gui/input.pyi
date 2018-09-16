#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import List

from swine.gui import Canvas
from swine.object import Component, GameObject
from .widget import Widget


class Input(Widget, GameObject):
    def __init__(self: Input, canvas: Canvas, name: str, components: List[Component], text: str, tags: List[str]=(), parent: GameObject=None, command: FunctionType=None, length: int=10, limit: int=None, disabled: bool=False) -> None:
        ...
