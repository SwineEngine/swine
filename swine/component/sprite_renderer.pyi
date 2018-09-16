#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet.sprite

from swine.object.component import Component
import swine.graphics
from swine.window import Layer


class SpriteRenderer(Component):
    def __init__(self: SpriteRenderer, image: swine.graphics.Sprite, layer: Layer, scale: int = 1) -> None:
        self.image: swine.graphics.Sprite = None
        self.layer: Layer = None
        self.scale: int = None

        self.sprite: pyglet.sprite.Sprite = None

    def move_rigid_to_parent(self: SpriteRenderer) -> None:
        ...
