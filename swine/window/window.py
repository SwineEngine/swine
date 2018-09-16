#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pyglet
from pymunk.pyglet_util import DrawOptions

from swine.input import InputManager
from swine.terminal.window import TerminalWindow
from swine.window import Scene
from swine.window.mainloop import Mainloop


class Window(pyglet.window.Window):
    def __init__(self, debug: bool = False):
        self.debug = debug

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

        self.terminal = None

        self.layers = []

        if self.debug:
            self.options = DrawOptions()

        self.clock.schedule(self.update)

    def on_close(self):
        self.close()

    def on_draw(self):
        self.clear()

        for batch in self.scene_list[self.active_scene].batch_list:
            batch.draw()

        for obj in self.scene_list[self.active_scene].object_list:
            for component in obj.components:
                component.draw()

        if self.debug:
            self.scene_list[self.active_scene].space.debug_draw(self.options)

    # End of abstract methods

    def mainloop(self):
        self._loop = Mainloop()
        self._loop.run()

    def close(self):
        self._loop.exit()
        pyglet.window.Window.close(self)

    def update(self, dt):
        self.scene_list[self.active_scene].space.step(dt)
        self.dispatch_event("on_update", dt)

        if self.terminal is not None:
            self.terminal.update()

    def get_layer_by_name(self, name: str):
        for layer in self.layers:
            if layer.name == name:
                return layer

        return None
