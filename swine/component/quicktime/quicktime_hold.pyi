#!/usr/bin/env python
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import Optional

from swine.input import InputManager
from swine.object import Component


class QuickTimeHold(Component):
    def __init__(self: QuickTimeHold, key: int, length: int, reset: str="instant", command: Optional[FunctionType]=None) -> None:
        self.key: int = None
        self.length: int = None
        self.reset: str = None
        self.command: Optional[FunctionType] = None

        self.current_length: int = None

        self.input: InputManager = None
