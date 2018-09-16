#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.image import AbstractImage

from swine.object import Anchor


class Sprite(object):
    def __init__(self: Sprite, image: str, anchor: Anchor, anchor_x: int = 0, anchor_y: int = 0) -> None:
        self.image: str = None
        self.anchor: Anchor = None
        self.anchor_x: int = None
        self.anchor_y: int = None

        self.sprite: AbstractImage = None
