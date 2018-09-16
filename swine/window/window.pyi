#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pyglet.clock import Clock
from pyglet.window import Window as PygWindow
from pyglet.input import Joystick

from swine.input import InputManager
from swine.terminal.window import TerminalWindow
from swine.window import Scene, Layer


class Window(PygWindow):
    def __init__(self: Window, debug: bool=False) -> None:
        self.debug: bool = None
        
        self.joystick: Joystick = None
        
        self.scene_list: List[Scene] = None
        self.active_scene: int = None
        
        self.clock: Clock = None
        
        self._loop: bool = None
        
        self.input_manager: InputManager = None
        
        self.terminal: TerminalWindow = None
        
        self.layers: List[Layer] = None

    def on_close(self: Window) -> None:
        ...

    def on_draw(self: Window) -> None:
        ...

    def mainloop(self: Window) -> None:
        ...

    def close(self: Window) -> None:
        ...

    def update(self: Window, dt: float) -> None:
        ...

    def get_layer_by_name(self: Window, name: str) -> None:
        ...
