#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pyglet

from swine.input import InputManager
from swine.window import Scene
from swine.window.mainloop import Mainloop


class Window(pyglet.window.Window):
    def __init__(self):
        joysticks = pyglet.input.get_joysticks()
        if len(joysticks) > 0:
            self.joystick = pyglet.input.get_joysticks()[0]
            self.joystick.open()
        else:
            self.joystick = None

        pyglet.window.Window.__init__(self, resizable=False, vsync=False, style=pyglet.window.Window.WINDOW_STYLE_DEFAULT)
        self.scene_list: List[Scene] = []
        self.active_scene = 0

        self.clock = pyglet.clock.get_default()

        self._loop = None
        self.register_event_type("on_update")

        self.input_manager = InputManager(self, self.joystick)

        self.clock.schedule(self.physics_update)

    def on_close(self):
        self.close()

    def on_draw(self):
        self.clear()

        for batch in self.scene_list[self.active_scene].batch_list:
            batch.draw()

    # End of abstract methods

    def mainloop(self):
        self._loop = Mainloop()
        self._loop.run()

    def close(self):
        self._loop.exit()
        pyglet.window.Window.close(self)

    def physics_update(self, dt):
        self.scene_list[self.active_scene].space.step(dt)
