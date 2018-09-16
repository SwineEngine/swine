#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.object import GameObject


class Component(object):
    def __init__(self: Component) -> None:
        self.parent: GameObject = None

        self.is_loaded: bool = None

    def start(self: Component) -> None:
        ...

    def update(self: Component, dt: float) -> None:
        ...

    def finish(self: Component) -> None:
        ...

    def physics_update(self: Component, dt: float) -> None:
        ...

    def collision_enter(self: Component, collider: GameObject) -> None:
        ...

    def collision_stay(self: Component, collider: GameObject) -> None:
        ...

    def collision_exit(self: Component, collider: GameObject) -> None:
        ...

    def draw(self: Component) -> None:
        ...

    def load(self: Component) -> None:
        ...

    def unload(self: Component) -> None:
        ...
