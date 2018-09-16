#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.graphics import Batch
import pymunk


class Scene(object):
    def __init__(self, window, gravity=pymunk.Vec2d(0, 0), drag=1, sleep_time=pymunk.inf):
        self.window = window
        self.gravity = gravity
        self.drag = drag
        self.sleep_time = sleep_time

        # Graphics
        self.batch = Batch()
        self.batch_list = [self.batch]

        # Objects
        self.object_list = []

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

        # Camera
        self.camera = None

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

    def get_object(self, name):
        for obj in self.object_list:
            if obj.name == name:
                return obj

        return None

    def get_object_with_component(self, type_):
        for obj in self.object_list:
            for comp in obj.components:
                if type(comp) == type_:
                    return obj

        return None
