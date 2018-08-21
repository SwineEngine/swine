#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.window import key
import pymunk
from pymunk import Vec2d

import swine.window
import swine.object
import swine.component
import swine.component.physics
import swine.component.physics.collider
import swine.graphics
from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.input.xbox_controller import XBoxController

window = swine.window.Window()

scene_one = swine.window.Scene(window, pymunk.Vec2d(0, 0), 0.1)


class PlayerMove(swine.object.Component):
    def __init__(self):
        swine.object.Component.__init__(self)
        self.input = None

        self.rigid: RigidBody = None

        self.speed = 300  # * dt
        self.increase = self.speed / 250000000000

    def start(self):
        self.input = self.parent.scene.window.input_manager

        self.rigid = self.parent.get_component(RigidBody)

    def update(self, dt):
        sprite = self.parent.get_component(SpriteRenderer)

        force = pymunk.Vec2d(0, 0)

        # Move Right
        if self.input.get_key(key.D) or self.input.get_joystick_hat(XBoxController.DIRECTIONAL_PAD_RIGHT):
            # print("Moving right")
            force.x = self.speed
            sprite.sprite.scale_x = 1

        left_thumb = self.input.get_joystick_axis(XBoxController.LEFT_THUMBSTICK_X)
        if left_thumb and left_thumb > 0.1:
            # print("Moving right (Thumbstick)")
            force.x = self.increase

            if force.x < self.speed:
                self.increase += left_thumb

            sprite.sprite.scale_x = 1

        elif left_thumb == 0:
            self.increase = 0

        # Move Left
        if self.input.get_key(key.A) or self.input.get_joystick_hat(XBoxController.DIRECTIONAL_PAD_LEFT):
            # print("Moving left")
            force.x = -self.speed
            sprite.sprite.scale_x = -1

        right_thumb = self.input.get_joystick_axis(XBoxController.LEFT_THUMBSTICK_X)
        if right_thumb and right_thumb < -0.1:
            # print("Moving left (Thumbstick)")
            force.x = self.increase

            if force.x > -self.speed:
                self.increase += right_thumb

            sprite.sprite.scale_x = -1

        elif left_thumb == 0:
            self.increase = 0

        if self.rigid is not None:
            self.rigid.add_force(force.x, force.y)


pig_sprite = swine.graphics.Sprite("pig_idle_0.png", swine.object.Anchor.MIDDLE_CENTER)
debug = swine.object.GameObject(scene_one, [PlayerMove(),
                                            swine.component.Transform(Vec2d(300, 300)),
                                            swine.component.SpriteRenderer(pig_sprite, 7),
                                            swine.component.physics.RigidBody(),
                                            swine.component.physics.collider.PolygonCollider()])

debug2 = swine.object.GameObject(scene_one, [swine.component.Transform(Vec2d(100, 300)),
                                             swine.component.SpriteRenderer(pig_sprite, 7),
                                             swine.component.physics.RigidBody(),
                                             swine.component.physics.collider.PolygonCollider()])

window.mainloop()
