#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene


class Polygon(GameObject):
    def __init__(self, scene, fill=True, point_total=0, x=0, y=0, layer=0, points=[], colours=[]):
        # type: (Scene, bool, int, int, int, int, list[int], list[str]) -> None
        GameObject.__init__(self, scene=scene)
        self.layer = layer
        self.scene = scene
        self.point_total = point_total
        self.points = points
        self.colours = self._colour_handler(colours)

        self.x_points = []
        self.y_points = []

        for i in range(0, len(self.points)):
            # If even
            if i & 1:
                self.y_points.append(self.points[i])

            else:
                self.x_points.append(self.points[i])

        self.size = (max(self.x_points) - min(self.x_points), max(self.y_points) - min(self.y_points))
        self.center = (self.size[0] / 2, self.size[1] / 2)

        if fill:
            mode = pyglet.gl.GL_POLYGON
        else:
            mode = pyglet.gl.GL_LINE_LOOP

        self.batch = pyglet.graphics.Batch()
        self.shape = self.batch.add(point_total, mode, None,
                                     ('v2f', self.points),
                                     ('c3B', self.colours))
        self.scene.batch_list.append(self.batch)

        self.scene.object_list.append(self)

    def _colour_handler(self, colours):
        if isinstance(colours, list):
            while len(colours) < self.point_total:
                colours.append(colours[-1])

            colours = tuple(sum(colours, ()))
        elif isinstance(colours, tuple):
            colours *= self.point_total

        return colours

    def colour(self, colours=[]):
        self.shape.colors = self._colour_handler(colours)

        return colours
