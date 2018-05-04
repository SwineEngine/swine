#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene


class Line(GameObject):
    def __init__(self, scene, width, height, x=0, y=0, layer=0, *colours):
        # type: (Scene, int, int, int, int, int, list[str]) -> None
        GameObject.__init__(self, scene=scene)
        self._layer = layer
        self._scene = scene
        self._x = x
        self._y = y

        required_colours = 2

        if len(colours) < required_colours:
            colours += colours

        colours = tuple(sum(colours, ()))

        scene.batch.add(2, pyglet.gl.GL_LINES, None,
                        ('v2i', (x, y, x + width, y + height)),
                        ('c3B', colours))

        self._scene.object_list.append(self)
