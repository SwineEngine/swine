#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.window import key
from pyglet.window import mouse
import pymunk

import swine.window
import swine.object
import swine.component
import swine.component.physics
import swine.graphics

window = swine.window.Window()

scene_one = swine.window.Scene(window, pymunk.Vec2d(0, -900), 0.1)


class PlayerMove(swine.object.Component):
    def __init__(self):
        swine.object.Component.__init__(self)
        self.input = None

    def start(self):
        self.input = self.parent.scene.window.input_manager

    def update(self):
        if self.input.get_key(key.W):
            print("W")

        if self.input.get_mouse_button(mouse.LEFT):
            print("Left")

        # print(self.input.get_joystick_button())


pig_sprite = swine.graphics.Sprite("pig_idle_0.png", swine.object.Anchor.MIDDLE_CENTER)
debug = swine.object.GameObject(scene_one, [PlayerMove(),
                                            swine.component.SpriteRenderer(pig_sprite, 6),
                                            swine.component.physics.RigidBody()])

window.mainloop()
