#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kytten import VerticalLayout, Label, Input, Scrollable, ANCHOR_LEFT, HorizontalLayout, Button
from pyglet.window import key

from swine.gui import Window
from swine.terminal.commands import CommandManager, Command
from swine.terminal.commands.standard import CommandHelp, CommandCommands


class TerminalWindow(object):
    def __init__(self, canvas, toggle_key=key.GRAVE):
        self.canvas = canvas
        self.toggle_key = toggle_key

        self.canvas.scene.window.terminal = self
        self.input_manager = self.canvas.scene.window.input_manager

        self.command_manager = CommandManager("/")
        self.command_manager.register(CommandHelp())
        self.command_manager.register(CommandCommands())

        self.text_lines = VerticalLayout(align=ANCHOR_LEFT)
        self.input = Input()

        self.scrollable = Scrollable(self.text_lines, width=canvas.scene.window.width, height=70, is_fixed_size=True)

        self.window = None

    def update(self):
        if self.input_manager.get_key(self.toggle_key):
            if self.window is None:
                self.window = Window(self.canvas, "Terminal", [], "Terminal", VerticalLayout([
                    self.scrollable,
                    HorizontalLayout([
                        Label(self.command_manager.prefix), self.input, Button("^", on_click=self.insert_line)
                    ])]))

    def insert_line(self):
        if self.input.get_text() != "":
            # self.text_lines.content.append(Label(self.input.get_text()))

            command_name = self.input.get_text().split(" ")[0]
            if command_name in self.command_manager.commands.keys():
                command = self.command_manager.commands[command_name]

                arguments = self.input.get_text().split(" ")
                arguments.pop(0)

                command.perform(self, self.text_lines, arguments)

            self.input.set_text("")
