#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict, List

from kytten import HorizontalLayout, VerticalLayout, GridLayout

from swine.terminal.window import TerminalWindow


class Command(object):
    def __init__(self: Command, name: str, args: Dict[str, type]=None, alias: str=None):
        self.name: str = None
        self.args: Dict[str, type] = None
        self.alias: str = None

    def perform(self: Command, terminal: TerminalWindow, output: HorizontalLayout or VerticalLayout or GridLayout=None, arguments: List[str]=None) -> None:
        ...

    def help(self: Command) -> str:
        ...

    def help_full(self: Command) -> str:
        ...
