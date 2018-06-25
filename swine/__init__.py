#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import json
import os

from .globals import *
from .window import Window
from .scene import Scene
from .gameobject import GameObject
from .sprite import Sprite
# from .gui import *
# from .shape import *

with open(os.path.join(os.path.dirname(__file__), "info.json")) as info:
    info_json = json.load(info)

    __title__ = info_json["name"]

    __author__ = info_json["author"]
    __copyright__ = info_json["copyright"]
    __credits__ = info_json["credits"]

    __license__ = info_json["license"]
    __version__ = info_json["version"]
    __maintainer__ = info_json["maintainer"]
    __email__ = info_json["author_email"]
    __status__ = info_json["status"]

del json
del os
