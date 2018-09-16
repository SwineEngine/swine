#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kytten import Label

from swine.terminal.commands import Command


class CommandCommands(Command):
    def __init__(self):
        Command.__init__(self, "commands")

    def perform(self, terminal, output=None, arguments=None):
        for c in terminal.command_manager.commands.keys():
            command = terminal.command_manager.commands[c]
            output.content.append(Label("{} - {}".format(c, command.name)))

    def help(self):
        return "Lists all registered commands"
