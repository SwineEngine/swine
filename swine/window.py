#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet
import os

from swine import Globals


class Window(pyglet.window.Window):
    def __init__(self, background=(240, 240, 240), resizable=False, vsync=False, debug=False, style=pyglet.window.Window.WINDOW_STYLE_DEFAULT):
        # type: (str) -> None
        pyglet.window.Window.__init__(self, resizable=resizable, vsync=vsync, style=style)
        self.debug = debug
        self.background = background
        self._resizeable = resizable
        self._vsync = vsync
        self._style = style

        self._title = ""
        self._icon = None
        self._fullscreen = False
        self._min_size = (0, 0)
        self._max_size = (0, 0)

        if self.debug:
            from pymunk.pyglet_util import DrawOptions

            self.options = DrawOptions()

        pyglet.gl.glClearColor(int(background[0]) / 255, int(background[1]) / 255, int(background[2]) / 255, 1)

        Globals.WINDOW = self

        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)

        self._loop = True

        self._middle = [self.width / 2, self.height / 2]

        self._mouse_x = 0
        self._mouse_y = 0
        
        self.scene_list = []
        self.active_scene = 0

        self.icon(pyglet.image.load(os.path.join(os.path.dirname(__file__), "swine.png")))

        self.clock = pyglet.clock.get_default()

        if Globals.FPS_LIMIT != -1:
            self.clock.set_fps_limit(Globals.FPS_LIMIT)

        if Globals.GUI_FPS != -1:
            self.clock.schedule_interval(self.gui_update, 1 / Globals.GUI_FPS)

        else:
            self.clock.schedule(self.gui_update)

        if Globals.PHYSICS_FPS != -1:
            self.clock.schedule_interval(self.physics_update, 1 / Globals.PHYSICS_FPS)

        else:
            self.clock.schedule(self.physics_update)

        self._benchmark_timer = 0
        self._benchmark_list = []

        self.register_event_type("on_update")

    def title(self, title):
        # type: (str) -> str
        """
        Set and return the title of the window.

        :param title:
        :return:
        """
        self._title = title
        self.set_caption(title)

        return self._title

    def icon(self, image):
        # type: (pyglet.image.AbstractImage) -> str
        """
        Sets and returns the icon of the window.

        :param image:
        :return:
        """
        self._icon = image
        self.set_icon(image)

        return self._icon

    def fullscreen(self, fullscreen):
        # type: (bool) -> bool
        """
        Set and return if the window is fullscreen.

        :param fullscreen:
        :return:
        """
        self._fullscreen = fullscreen
        self.set_fullscreen(fullscreen)

        return self._fullscreen

    def min_size(self, width, height):
        # type: (int, int) -> tuple[int, int]
        """
        Set and return the minimum size of the window.

        :param width:
        :param height:
        :return:
        """
        self._min_size = (width, height)
        self.set_minimum_size(width, height)

        return self._min_size

    def max_size(self, width, height):
        # type: (int, int) -> tuple[int, int]
        """
        Set and return the maximum size of the window.

        :param width:
        :param height:
        :return:
        """
        self._max_size = (width, height)
        self.set_maximum_size(width, height)

        return self._max_size

    def size(self, width, height):
        # type: (int, int) -> tuple[int, int]
        """
        Set and return the size of the window.

        :param width:
        :param height:
        :return:
        """
        self.set_size(width, height)

        return self.get_size()

    def location(self, x, y):
        # type: (int, int) -> tuple[int, int]
        """
        Set and return the location of the window.

        :param x:
        :param y:
        :return:
        """
        self.set_location(x, y)

        return self.get_location()

    def mainloop(self):
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

        while self._loop:
            pyglet.clock.tick()

            try:
                for window in pyglet.app.windows:
                    try:
                        window.switch_to()
                        window.dispatch_events()
                        window.dispatch_event('on_draw')
                        window.flip()

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

        if self.debug:
            self.scene_list[self.active_scene].space.debug_draw(self.options)

    def on_key_press(self, symbol, modifiers):
        for item in self.scene_list[self.active_scene].object_list:
            item.key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for item in self.scene_list[self.active_scene].object_list:
            item.key_release(symbol, modifiers)

    def on_text(self, text):
        for item in self.scene_list[self.active_scene].object_list:
            try:
                item.text(text)

            except TypeError:
                pass

    def on_text_motion(self, motion):
        for item in self.scene_list[self.active_scene].object_list:
            item.text_motion(motion)

    def on_mouse_motion(self, x, y, dx, dy):
        self._mouse_x = x
        self._mouse_y = y

        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_release(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_enter(self, x, y):
        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_enter(x, y)

    def on_mouse_leave(self, x, y):
        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_leave(x, y)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        for item in self.scene_list[self.active_scene].object_list:
            item.mouse_scroll(x, y, scroll_x, scroll_y)

    #####

    def gui_update(self, dt):
        self.dispatch_event("on_update", dt)

    def physics_update(self, dt):
        self.scene().space.step(dt)

    def scene(self):
        return self.scene_list[self.active_scene]

    def mouse_position(self):
        return -(self._middle[0] - self._mouse_x), -(self._middle[1] - self._mouse_y)

    def benchmark(self, time):
        self._benchmark_timer = time

        print("Starting benchmark")

        self.clock.schedule(self.benchmark_update)

    def benchmark_update(self, event):
        if self._benchmark_timer > 0:
            self._benchmark_list.append(self.clock.get_fps())
            self._benchmark_timer -= 1

        else:
            self.clock.unschedule(self.benchmark_update)

            if 0 in self._benchmark_list:
                self._benchmark_list.remove(0)

            self.benchmark_end(min(self._benchmark_list), max(self._benchmark_list), sum(self._benchmark_list) / float(len(self._benchmark_list)))

    def benchmark_end(self, min_, max_, average):
        print(f"Minimum FPS: {min_}\nMaximum FPS: {max_}\nAverage FPS: {average}")

        self.close()


