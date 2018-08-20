#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk

import swine.window
import swine.object
import swine.component
import swine.component.physics
import swine.graphics

window = swine.window.Window()

scene_one = swine.window.Scene(window, pymunk.Vec2d(0, -900), 0.1)


class DebugPrint(swine.object.Component):
    def start(self):
        print("Start")

    def update(self):
        pass  # print("Update")


pig_sprite = swine.graphics.Sprite("pig_idle_0.png", swine.object.Anchor.MIDDLE_CENTER)
debug = swine.object.GameObject(scene_one, [DebugPrint(),
                                            swine.component.SpriteRenderer(pig_sprite, 6),
                                            swine.component.physics.RigidBody()])

window.mainloop()
