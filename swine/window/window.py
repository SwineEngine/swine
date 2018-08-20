#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pyglet

from .scene import Scene


class Window(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, resizable=False, vsync=False, style=pyglet.window.Window.WINDOW_STYLE_DEFAULT)
        self.scene_list: List[Scene] = []
        self.active_scene = 0

        self.clock = pyglet.clock.get_default()

        self._loop = True
        self.register_event_type("on_update")

    def mainloop(self):
        while self._loop:
            pyglet.clock.tick()

            try:
                for window in pyglet.app.windows:
                    try:
                        window.switch_to()
                        window.dispatch_events()
                        window.dispatch_event('on_draw')
                        window.flip()

                        for obj in window.scene_list[window.active_scene].object_list:
                            obj.update()

                    except AttributeError:
                        pass

            except RuntimeError:
                pass

    def close(self):
        self._loop = False
        pyglet.window.Window.close(self)

    def on_close(self):
        self.close()

    def on_draw(self):
        self.clear()

        for batch in self.scene_list[self.active_scene].batch_list:
            batch.draw()
