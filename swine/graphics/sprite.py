#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyglet.image import load

from swine.object import Anchor


class Sprite(object):
    def __init__(self, image: str, anchor: Anchor, anchor_x: int = None, anchor_y: int = None):
        self.image = image
        self.anchor = anchor
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

        self.sprite = load(self.image)

        if self.anchor == Anchor.CUSTOM:
            self.sprite.anchor_x = self.anchor_x
            self.sprite.anchor_y = self.anchor_y

        elif self.anchor == Anchor.MIDDLE_CENTER:
            self.sprite.anchor_x = self.sprite.width // 2
            self.sprite.anchor_y = self.sprite.height // 2
