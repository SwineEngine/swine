#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

# import soloud

from swine.sound import Group
from swine.window.scene import Scene


class Mixer(object):
    def __init__(self, scene: Scene, groups: List[Group]):
        self.scene = scene
        self.groups = groups

        # self.audolib = soloud.Soloud()
        # self.audolib.init(self.audolib.CLIP_ROUNDOFF |
        #                   self.audolib.ENABLE_VISUALIZATION)

        self.scene.mixers.append(self)

    def create_group(self, channel: str, volume: int = 1):
        pass

    def set_group_volume(self, channel: str, volume: int):
        pass

    def remove(self):
        # self.audolib.deinit()
        self.scene.mixers.remove(self)
