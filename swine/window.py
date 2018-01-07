#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

class Window(pyglet.window.Window):
    def __init__(self, style=pyglet.window.Window.WINDOW_STYLE_DEFAULT, vsync=False):
        # type: (str) -> None
        pyglet.window.Window.__init__(self, style=style, vsync=vsync)

        self._title = ""
        self._icon = None
        self._fullscreen = False
        self._min_size = (0, 0)
        self._max_size = (0, 0)

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
        while True:
            pyglet.clock.tick()

            for window in pyglet.app.windows:
                window.switch_to()
                window.dispatch_events()
                window.dispatch_event('on_draw')
                window.flip()

    def on_draw(self):
        self.clear()
