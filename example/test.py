#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.window import key
import pymunk

import swine.window
import swine.object
import swine.component
import swine.component.physics
import swine.graphics
from swine.input.xbox_controller import XBoxController

window = swine.window.Window()

scene_one = swine.window.Scene(window, pymunk.Vec2d(0, -900), 0.1)


class PlayerMove(swine.object.Component):
    def __init__(self):
        swine.object.Component.__init__(self)
        self.input = None

    def start(self):
        self.input = self.parent.scene.window.input_manager

    def update(self):
        # Move Right
        if self.input.get_key(key.D) or self.input.get_joystick_hat(XBoxController.DIRECTIONAL_PAD_RIGHT):
            print("Moving right")

        if self.input.get_joystick_axis(XBoxController.LEFT_THUMBSTICK_X) and self.input.get_joystick_axis(XBoxController.LEFT_THUMBSTICK_X) > 0.1:
            print("Moving right (Thumbstick)")

        # Move Left
        if self.input.get_key(key.A) or self.input.get_joystick_hat(XBoxController.DIRECTIONAL_PAD_LEFT):
            print("Moving left")

        if self.input.get_joystick_axis(XBoxController.LEFT_THUMBSTICK_X) and self.input.get_joystick_axis(XBoxController.LEFT_THUMBSTICK_X) < -0.1:
            print("Moving left (Thumbstick)")


pig_sprite = swine.graphics.Sprite("pig_idle_0.png", swine.object.Anchor.MIDDLE_CENTER)
debug = swine.object.GameObject(scene_one, [PlayerMove(),
                                            swine.component.Transform(),
                                            swine.component.SpriteRenderer(pig_sprite, 6),
                                            swine.component.physics.RigidBody()])

window.mainloop()
