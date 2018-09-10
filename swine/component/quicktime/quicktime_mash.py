#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.object import Component


class QuickTimeMash(Component):
    def __init__(self, key, times: int, press_cooldown=70, command=None):
        Component.__init__(self)
        self.key = key
        self.times = times
        self.press_cooldown = press_cooldown
        self.command = command

        self.current_times = 0

        self.input = None

    def start(self):
        self.input = self.parent.scene.window.input_manager

    def update(self, dt):
        if self.input.get_key(self.key):
            if self.current_times >= self.times:
                self.command()

            else:
                self.current_times += 1 / self.press_cooldown
