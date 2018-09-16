#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kytten import VerticalLayout, Input, Scrollable
from pyglet.window import key

from swine.gui import Window, Canvas
from swine.input import InputManager
from swine.terminal.commands import CommandManager


class TerminalWindow(object):
    def __init__(self: TerminalWindow, canvas: Canvas, toggle_key: int=key.GRAVE):
        self.canvas: Canvas = None
        self.toggle_key: int = None

        self.input_manager: InputManager = None

        self.command_manager: CommandManager = None

        self.text_lines: VerticalLayout = None
        self.input: Input = None

        self.scrollable: Scrollable = None

        self.window: Window = None

    def update(self: TerminalWindow) -> None:
        ...

    def insert_line(self: TerminalWindow) -> None:
        ...
