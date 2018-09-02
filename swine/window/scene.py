#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Optional

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

        # Sounds
        self.mixers = []

        # Physics
        self.space = pymunk.Space()
        self.space.gravity = self.gravity
        self.space.damping = self.drag
        self.space.sleep_time_threshold = self.sleep_time

        # Collisions
        self.handler = self.space.add_default_collision_handler()
        self.handler.begin = self.collision_enter
        self.handler.post_solve = self.collision_stay

        self.handler.separate = self.collision_exit

        # Other
        self.window.scene_list.append(self)

    # Listeners

    def collision_enter(self, arbiter, space, data):
        for shape in arbiter.shapes:
            try:
                shape.parent.parent.collision_enter(self.collision(arbiter, shape))

            except AttributeError:
                pass

        return True

    def collision_stay(self, arbiter, space, data):
        for shape in arbiter.shapes:
            try:
                shape.parent.parent.collision_stay(self.collision(arbiter, shape))

            except AttributeError:
                pass

        return True

    def collision_exit(self, arbiter, space, data):
        for shape in arbiter.shapes:
            try:
                shape.parent.parent.collision_exit(self.collision(arbiter, shape))

            except AttributeError:
                pass

        pass

    @staticmethod
    def collision(arbiter, shape):
        try:
            col = arbiter.shapes[not arbiter.shapes[arbiter.shapes.index(shape)]].parent

        except AttributeError:
            col = arbiter.shapes[not arbiter.shapes[arbiter.shapes.index(shape)]]

        return col

    # Methods

    def get_object(self, name: str):  # -> Optional[GameObject]:
        for obj in self.object_list:
            if obj.name == name:
                return obj

        return None
