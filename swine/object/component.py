#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Component(object):
    def __init__(self):
        self.parent = None

    def start(self):
        pass

    def update(self):
        pass

    def physics_update(self):
        pass
