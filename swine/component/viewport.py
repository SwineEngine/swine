#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk
from pyglet.gl import glViewport, glLoadIdentity, glTranslatef, glRotatef

from swine.component import Transform
from swine.object.component import Component


class Viewport(Component):
    def __init__(self, size: pymunk.Vec2d = pymunk.Vec2d(640, 480)):
        Component.__init__(self)
        self.size = size

        self.first_update = True

    def update(self, dt):
        if self.first_update:
            self.first_update = False

            glViewport(0, 0, self.size.x, self.size.y)

        transform = self.parent.get_component(Transform)

        pos_x = 0
        pos_y = 0
        rotation = 0
        if transform is not None:
            pos_x = transform.position.x
            pos_y = transform.position.y
            rotation = transform.rotation

        glLoadIdentity()
        glRotatef(rotation, 0, 0, -1)
        glTranslatef(-pos_x + (self.size.x / 2), -pos_y + (self.size.y / 2), 0)

