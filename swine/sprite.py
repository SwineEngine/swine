#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

# import pyglet

import rabbyt

from swine import GameObject
from swine import Scene


class Sprite(GameObject):  #, pyglet.sprite.Sprite):
    def __init__(self, scene, frames=[], fps=None, scale=1, layer=0):
        # type: (Scene, list) -> None
        GameObject.__init__(self, scene)
        self.layer = layer
        # pyglet.sprite.Sprite.__init__(self, img=image, batch=scene.batch, group=scene.layers[self.layer])
        self.scene = scene
        self.frames = frames
        self.scale = scale

        if fps is None:
            self.fps = len(frames) * 2

        else:
            self.fps = fps

        self.rabbyt_frames = []

        for i in self.frames:
            self.rabbyt_frames.append(rabbyt.pyglet_load_texture(i))

        self.sprite = rabbyt.Sprite(self.rabbyt_frames[0])
        self.sprite.scale = self.scale

        self.scene.sprite_list.append(self)

        self._frame = 0

        self.scene.window.clock.schedule_interval(self.animation_update, 1 / self.fps)

    def animation_update(self, dt=None):
        self.sprite.texture = self.rabbyt_frames[self._frame]

        if self._frame < len(self.frames) - 1:
            self._frame += 1

        else:
            self._frame = 0
