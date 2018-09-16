#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict

from swine.terminal.commands.command import Command


class CommandManager(object):
    def __init__(self: CommandManager, prefix: str):
        self.prefix: str = None
        self.commands: Dict[str, Command] = None

    def register(self: CommandManager, command: Command) -> None:
        ...
