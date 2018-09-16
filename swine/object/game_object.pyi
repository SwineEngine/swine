#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Optional, Type, TypeVar

from swine.window import Scene

from swine.object import Component


T = TypeVar('T')


class GameObject(object):
    def __init__(self: GameObject, scene, name: str, components: List[Component], tags: List[str]=(), parent: GameObject=None, never_reload: bool=False) -> None:
        self.scene: Scene = None
        self.name: str = None
        self.components: List[Component] = None
        self.never_reload: bool = None

        self.pre_load: bool = None
        self.is_loaded: bool = None

        self.parent: GameObject = None
        self.children: List[GameObject] = None

        self.id: int = None

        self.tags: List[str] = None

    def start(self: GameObject) -> None:
        ...

    def update(self: GameObject, dt: Optional[float]=None) -> None:
        ...

    def physics_update(self: GameObject, dt: Optional[float]=None) -> None:
        ...

    def collision_enter(self: GameObject, collider: GameObject) -> None:
        ...

    def collision_stay(self: GameObject, collider: GameObject) -> None:
        ...

    def collision_exit(self: GameObject, collider: GameObject) -> None:
        ...

    def load(self: GameObject) -> None:
        ...

    def unload(self: GameObject) -> None:
        ...

    def flip_load(self: GameObject) -> None:
        ...

    def set_parent(self: GameObject, parent) -> None:
        ...

    def get_component(self: GameObject, type_: Type[T]) -> Optional[T]:
        ...

    def get_multiple_components(self: GameObject, type_: Type[T]) -> List[T]:
        ...
