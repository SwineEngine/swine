#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import subprocess
import pip
import shutil

from pip._internal.utils.misc import get_installed_distributions

if __name__ == "__main__":
    # Remove the built files
    if os.path.isdir("dist"):
        shutil.rmtree("dist")

    packages = [package.project_name for package in get_installed_distributions()]

    # Install packages
    if "wheel" not in packages:
        pip._internal.main(['install', "wheel"])

    if "twine" not in packages:
        pip._internal.main(['install', "twine"])

    # Build the package and a wheel
    subprocess.call(["python", "setup.py", "sdist", "bdist_wheel"])

    for f in os.listdir("dist"):
        match = re.match(pattern="swine-[0-9].[0-9].[0-9]-py(2|3)-none-any.whl+", string=f)
        if match:
            subprocess.call(["pip3", "install", f"dist/{match.string}", "--upgrade"])

    # Upload the package
    subprocess.call(["twine", "upload", "dist/*"])
