#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
import pymunk

from swine import Window


class Scene(object):
    def __init__(self, window, layer_count=25, gravity=pymunk.Vec2d(0, 0), drag=1, sleep_time=pymunk.inf):
        # type: (Window) -> None
        self.window = window
        self.layer_count = layer_count
        self.gravity = gravity
        self.drag = drag
        self.sleep_time = sleep_time

        self.id = len(self.window.scene_list)
        self.batch = pyglet.graphics.Batch()
        self.batch_list = [self.batch]
        self.object_list = []
        self.physics_list = []

        self.layers = []
        for number in range(self.layer_count):
            self.layers.append(pyglet.graphics.OrderedGroup(number))

        self.space = pymunk.Space()
        self.space.gravity = self.gravity
        self.space.damping = self.drag
        self.space.sleep_time_threshold = self.sleep_time

        self.handler = self.space.add_default_collision_handler()
        self.handler.begin = self.collision_enter
        self.handler.post_solve = self.collision_stay
        self.handler.separate = self.collision_exit

        self.window.scene_list.append(self)

    def collision_enter(self, arbiter, space, data):
        for shape in arbiter.shapes:
            try:
                shape.parent.collision_enter(self.collision(arbiter, shape))

            except AttributeError:
                pass

        return True

    def collision_stay(self, arbiter, space, data):
        for shape in arbiter.shapes:
            try:
                shape.parent.collision_stay(self.collision(arbiter, shape))

            except AttributeError:
                pass

        return True

    def collision_exit(self, arbiter, space, data):
        for shape in arbiter.shapes:
            try:
                shape.parent.collision_exit(self.collision(arbiter, shape))

            except AttributeError:
                pass

        pass

    def collision(self, arbiter, shape):
        col = None

        try:
            col = arbiter.shapes[not arbiter.shapes[arbiter.shapes.index(shape)]].parent

        except AttributeError:
            col = arbiter.shapes[not arbiter.shapes[arbiter.shapes.index(shape)]]

        return col
