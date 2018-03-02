#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import json
from setuptools import setup

with open("swine/info.json") as info:
    info_json = json.load(info)

    setup(name=info_json["name"],
          version=info_json["version"],
          description=info_json["description"],
          author=info_json["author"],
          author_email=info_json["author_email"],
          url=info_json["url"],
          license=info_json["license"],
          classifiers=info_json["classifiers"],
          keywords=info_json["keywords"],
          packages=info_json["packages"],
          install_requires=["pyglet"])
