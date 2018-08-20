#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pyglet.graphics import Batch
import pymunk


class Scene(object):
    def __init__(self, window, gravity: pymunk.Vec2d = pymunk.Vec2d(0, 0), drag: float = 1, sleep_time: float = pymunk.inf):
        self.window = window
        self.gravity = gravity
        self.drag = drag
        self.sleep_time = sleep_time

        # Graphics
        self.batch = Batch()
        self.batch_list: List[Batch] = [self.batch]

        # Objects
        self.object_list = []

        # Physics
        self.space = pymunk.Space()
        self.space.gravity = self.gravity
        self.space.damping = self.drag
        self.space.sleep_time_threshold = self.sleep_time

        # Other
        self.window.scene_list.append(self)
