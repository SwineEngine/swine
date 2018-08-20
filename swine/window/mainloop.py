#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet
from pyglet.app.base import EventLoop


class Mainloop(EventLoop):
    def __init__(self):
        EventLoop.__init__(self)

    def idle(self):
        try:
            for window in pyglet.app.windows:
                try:
                    window.switch_to()
                    window.dispatch_events()
                    window.dispatch_event('on_draw')
                    window.flip()

                    for obj in window.scene_list[window.active_scene].object_list:
                        obj.update()
                        obj.physics_update()

                except AttributeError:
                    pass

        except RuntimeError:
            pass

        return self.clock.get_sleep_time(True)
