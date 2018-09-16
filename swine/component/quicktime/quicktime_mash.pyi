#!/usr/bin/env python
# -*- coding: utf-8 -*-
from types import FunctionType
from typing import Optional

from swine.input import InputManager
from swine.object.component import Component


class QuickTimeMash(Component):
    def __init__(self: QuickTimeMash, key: int, times: int, press_cooldown=70, command: Optional[FunctionType]=None) -> None:
        self.key: int = None
        self.times: int = None
        self.press_cooldown: int = None
        self.command: Optional[FunctionType] = None

        self.current_times: int = None

        self.input: InputManager = None
