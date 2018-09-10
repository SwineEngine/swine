#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

import pymunk

from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.object.component import Component


class Transform(Component):
    def __init__(self, position: pymunk.Vec2d = pymunk.Vec2d(0, 0), rotation: int = 0, scale: pymunk.Vec2d = pymunk.Vec2d(1, 1)):
        Component.__init__(self)
        self.position = position
        self.rotation = rotation
        self.scale = scale

        self.first_update = True

        self.sprite = None
        self.rigid = None

    def start(self):
        self.sprite = self.parent.get_component(SpriteRenderer)
        self.rigid = self.parent.get_component(RigidBody)

    def update(self, dt):
        if self.first_update:
            self.first_update = False

            from swine.gui import Widget
            if self.parent.parent is None and isinstance(self.parent, Widget):
                self.parent.offset = (self.position.x,
                                      self.position.y)
                self.parent.do_layout()

            window = self.parent.scene.window
            self.position = pymunk.Vec2d(self.position.x + (window.width / 2), self.position.y + (window.height / 2))

            if self.rigid is not None:
                self.rigid.body.angle = math.radians(self.rotation)
                self.rigid.body.position = self.position

        if self.sprite is not None:
            self.sprite.sprite.position = self.position.x, self.position.y
            self.sprite.sprite.rotation = math.degrees(-self.rotation)

            if self.parent.parent is not None:
                parent_transform = self.parent.parent.get_component(Transform)
                if parent_transform is not None:
                    self.scale = parent_transform.scale

            self.sprite.sprite.scale_x = self.scale[0]
            self.sprite.sprite.scale_y = self.scale[1]

        # Rigid Body
        if self.rigid is not None and self.parent.parent is None:
            self.rigid.body.angle = math.radians(self.rotation)
            self.position = self.rigid.body.position

        elif self.rigid is not None and self.parent.parent is not None:
            self.rigid.body.angle = math.radians(self.rotation)
            self.move_rigid_to_parent()

    def move_rigid_to_parent(self):
        parent_transform: Transform = self.parent.parent.get_component(Transform)
        child_transform: Transform = self.parent.get_component(Transform)

        if parent_transform is not None and child_transform is not None:
            window = self.parent.scene.window
            parent_position = parent_transform.position
            child_position = child_transform.position

            if self.scale.x == 1:
                new_x = (child_position.x + parent_position.x) - (window.width / 2)
            elif self.scale.x == -1:
                new_x = (-child_position.x + parent_position.x) + (window.width / 2)

            if self.scale.y == 1:
                new_y = (child_position.y + parent_position.y) - (window.height / 2)
            elif self.scale.y == -1:
                new_y = (-child_position.y + parent_position.y) + (window.height / 2)

            self.rigid.body.position = pymunk.Vec2d(new_x, new_y)
