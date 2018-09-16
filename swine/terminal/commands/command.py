#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict


class Command(object):
    def __init__(self, name: str, args: Dict[str, type]=None, alias: str=None):
        self.name = name
        self.args = args
        self.alias = alias

    def perform(self, terminal, output=None, arguments=None):
        pass

    def help(self):
        return "This command has no help"

    def help_full(self):
        str_args = ""

        if self.args is not None:
            for k, v in self.args.items():
                str_args += "{} - {}".format(k, v.__name__)

        else:
            str_args = "none"

        return self.help() + " | Args: " + str_args
