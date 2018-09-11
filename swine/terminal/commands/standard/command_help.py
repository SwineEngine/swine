#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kytten import Label

from swine.terminal.commands import Command


class CommandHelp(Command):
    def __init__(self):
        Command.__init__(self, "help", {"command": str}, "?")

    def perform(self, terminal, output=None, arguments=None):
        if arguments:
            command = terminal.command_manager.commands[arguments[0]]
            output.content.append(Label(f"{command.name} - {command.help_full()}"))

        else:
            for c in terminal.command_manager.commands:
                command = terminal.command_manager.commands[c]
                output.content.append(Label(f"{c} - {command.help()}"))

    def help(self):
        return "Lists the help for command/s"
