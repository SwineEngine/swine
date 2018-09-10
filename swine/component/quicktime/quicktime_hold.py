#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.object import Component


class QuickTimeHold(Component):
    def __init__(self, key, length: int, reset="instant", command=None):
        Component.__init__(self)
        self.key = key
        self.length = length
        self.reset = reset
        self.command = command

        self.current_length = 0

        self.input = None

    def start(self):
        self.input = self.parent.scene.window.input_manager

    def update(self, dt):
        if self.input.get_key(self.key):
            if self.current_length < self.length:
                self.current_length += 1

            else:
                self.command()

        else:
            if self.reset == "instant":
                self.current_length = 0

            elif self.reset == "slow":
                self.current_length -= 1

            elif self.reset == "none":
                pass
