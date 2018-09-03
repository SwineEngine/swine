#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name="swine",
      version="2.0.0",
      description="A Python game engine",
      author="DeflatedPickle",
      url="https://github.com/SwineProject/swine",
      license="MIT",
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6"
      ],
      keywords=["swine", "game", "engine", "game engine"],
      packages=["swine",
                "swine/component",
                "swine/component/physics", "swine/component/physics",
                "swine/graphics",
                "swine/input", "swine/input/handler",
                "swine/object",
                "swine/window"],
      install_requires=["pyglet", "pymunk"])
