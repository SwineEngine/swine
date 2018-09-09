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
        self.x = 0
        self.y = 0
        self.angle = 0

        self.first_update = True

    def update(self, dt):
        if self.parent == self.parent.scene.camera:
            if self.first_update:
                self.first_update = False

                glViewport(0, 0, self.size.x, self.size.y)

            # canvas = self.parent.scene.get_object("Canvas")
            # if canvas is not None:
            #     canvas.batch.draw()

            transform = self.parent.get_component(Transform)

            pos_x = 0
            pos_y = 0
            rotation = 0
            if transform is not None:
                pos_x = transform.position.x
                pos_y = transform.position.y
                rotation = transform.rotation

            glLoadIdentity()

            self.angle = rotation
            glRotatef(self.angle, 0, 0, -1)

            self.x = -pos_x + (self.size.x / 2)
            self.y = -pos_y + (self.size.y / 2)
            glTranslatef(self.x, self.y, 0)

