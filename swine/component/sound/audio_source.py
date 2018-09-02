#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.object import Component
# from swine.sound import Group


class AudioSource(Component):
    def __init__(self, mixer, file: str, group, mute: bool = False, loop: bool = False):
        Component.__init__(self)
        self.mixer = mixer
        self.file = file
        self.group = group
        self.mute = mute
        self.loop = loop

    def play(self):
        # self.mixer.audolib.play(self.file, self.group.volume)
        pass

    def stop(self):
        pass
