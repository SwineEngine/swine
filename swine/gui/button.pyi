#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import List

from swine.gui import Widget, Canvas
from swine.object import GameObject
from swine.object.component import Component


class Button(Widget, GameObject):
    def __init__(self: Button, canvas: Canvas, name: str, components: List[Component], text: str, tags: List[str]=(), parent: GameObject=None, command: FunctionType=None, disabled: bool=False) -> None:
        ...
