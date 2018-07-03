#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

# import pyglet

import rabbyt

from swine import GameObject, Scene, Globals


class Sprite(GameObject):  #, pyglet.sprite.Sprite):
    def __init__(self, scene, frames={}, begin=None, fps=None, scale=1, layer=0):
        # type: (Scene, dict) -> None
        GameObject.__init__(self, scene)
        self.layer = layer
        # pyglet.sprite.Sprite.__init__(self, img=image, batch=scene.batch, group=scene.layers[self.layer])
        self.scene = scene
        self.frames = frames
        self.begin = begin
        self.scale = scale
        self.fps = fps

        self._current = begin

        self.sprite = rabbyt.Sprite(self.load_frames(self.frames[self._current])[0])
        self.sprite.scale = self.scale

        self.scene.sprite_list.append(self)

        self.frame = 0

        self.rabbyt_frames = []

        self.rabbyt_frames = self.load_frames(self.frames[self._current])
        if self.begin is not None:
            self.play_animation(self._current)

        self.scene.window.clock.schedule_interval(self.animation_update, 1 / self.fps)

        self.paused = False

        self._wait_counter = 0
        self._pause_counter = 0

    def animation_update(self, dt=None):
        try:
            self.sprite.texture = self.rabbyt_frames[self.frame]

        except IndexError:
            pass

        if self.frame < len(self.rabbyt_frames) - 1:
            self.frame += 1

        else:
            self.frame = 0

    def load_frames(self, frames):
        rabbyt_frames = []

        for i in frames:
            rabbyt_frames.append(rabbyt.pyglet_load_texture(i))

        return rabbyt_frames

    def play_animation(self, animation):
        self.rabbyt_frames = self.load_frames(self.frames[animation])

        if self.fps is None:
            self.fps = len(self.frames[self._current]) * 2

    def pause_animation(self, length=-1):
        if length == -1:
            self.stop_animation()
            return

        else:
            self.stop_animation()
            self.paused = True

            self._pause_counter = length
            self.scene.window.clock.schedule_interval(self._tick_paused, 1 / Globals.SPRITE_FPS)

    def _tick_paused(self, length):
        if self._pause_counter > 0:
            self._pause_counter -= 1

        else:
            self.scene.window.clock.unschedule(self._tick_paused)
            self.unpause_animation()

    def unpause_animation(self):
        self.paused = False
        self.scene.window.clock.schedule_interval(self.animation_update, 1 / self.fps)

    def stop_animation(self):
        self.scene.window.clock.unschedule(self.animation_update)

    def reset_animation(self):
        self.frame = 0
