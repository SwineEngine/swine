#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Optional, Type

import pymunk
from pyglet.graphics import Batch
from pymunk import CollisionHandler, Space, Arbiter

from swine.object import GameObject
from swine.object.component import Component
from swine.window import Window


class Scene(object):
    def __init__(self: Scene, window: Window, gravity: pymunk.Vec2d = pymunk.Vec2d(0, 0), drag: float = 1, sleep_time: float = pymunk.inf) -> None:
        self.window: Window = None
        self.gravity: pymunk.Vec2d = None
        self.drag: float = None
        self.sleep_time: float = None

        self.batch: Batch = None
        self.batch_list: List[Batch] = None

        self.object_list: List[GameObject] = None

        self.space: Space = None

        self.handler: CollisionHandler = None

        self.camera: GameObject = None

    def collision_enter(self: Scene, arbiter: Arbiter, space: Space, data):
        ...

    def collision_stay(self: Scene, arbiter: Arbiter, space: Space, data):
        ...

    def collision_exit(self: Scene, arbiter: Arbiter, space: Space, data):
        ...

    @staticmethod
    def collision(arbiter: Arbiter, shape):
        ...

    def get_object(self: Scene, name: str) -> Optional[GameObject]:
        ...

    def get_object_with_component(self: Scene, type_: Type[Component]):
        ...
