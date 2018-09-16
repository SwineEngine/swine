#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import TypeVar

from kytten import Dialog

from swine.gui import Canvas


T = TypeVar('T')


class Widget(Dialog):
    def __init__(self: Widget, canvas: Canvas, widget: T, x: int =0, y: int =0) -> None:
        self.widget: T = None
