#!/usr/bin/env python
# -*- coding: utf-8 -*-

import swine.window
import swine.object

window = swine.window.Window()

scene_one = swine.window.Scene(window)


class DebugPrint(swine.object.Behaviour):
    def start(self):
        print("Start")

    def update(self):
        print("Update")


debug = swine.object.GameObject(scene_one, [DebugPrint()])

window.mainloop()
