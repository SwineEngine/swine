#!/usr/bin/env python
# -*- coding: utf-8 -*-

import swine.window
import swine.object
import swine.component
import swine.graphics

window = swine.window.Window()

scene_one = swine.window.Scene(window)


class DebugPrint(swine.object.Component):
    def start(self):
        print("Start")

    def update(self):
        print("Update")


pig_sprite = swine.graphics.Sprite("pig_idle_0.png", swine.object.Anchor.MIDDLE_CENTER)
debug = swine.object.GameObject(scene_one, [DebugPrint(),
                                            swine.component.SpriteRenderer(pig_sprite, 6)])

window.mainloop()
