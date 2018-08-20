#!/usr/bin/env python
# -*- coding: utf-8 -*-


class JoyStickStateHandler(object):
    def __init__(self):
        self.button = {}
        self.hat = (0, 0)
        self.axis = {}

    def on_joybutton_press(self, joystick, button):
        self.button[button] = True

    def on_joybutton_release(self, joystick, button):
        self.button[button] = False

    def on_joyhat_motion(self, joystick, hat_x, hat_y):
        self.hat = (hat_x, hat_y)

    def on_joyaxis_motion(self, joystick, axis, value):
        self.axis[axis] = value
