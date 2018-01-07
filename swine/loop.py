#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

window = pyglet.window.Window()

while True:
    pyglet.clock.tick()

    for window in pyglet.app.windows:
        window.switch_to()
        window.dispatch_events()
        window.dispatch_event('on_draw')
        window.flip()