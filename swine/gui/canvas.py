#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pyglet.graphics import Batch

from swine.object import GameObject, Component


class Canvas(GameObject):
    def __init__(self, scene, name, components: List[Component], tags: List[str]=()):
        GameObject.__init__(self, scene, name, components, tags)

        self.batch = Batch()
