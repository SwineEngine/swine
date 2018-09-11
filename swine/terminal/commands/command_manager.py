#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CommandManager(object):
    def __init__(self, prefix):
        self.prefix = prefix
        self.commands = {}

    def register(self, command):
        self.commands[command.name] = command

        if command.alias is not None:
            self.commands[command.alias] = command
